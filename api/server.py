"""
FastAPI接口服务

作用：
提供代码审查API
"""


from fastapi import FastAPI


from agent.code_review_agent import CodeReviewAgent


from pydantic import BaseModel

class ReviewRequest(BaseModel):
    code: str
    language: str = "python"


# 创建FastAPI应用

app = FastAPI(
    title="Smart Code Review Agent"
)



# 创建Agent

agent = CodeReviewAgent()



@app.get("/")
def home():

    return {

        "message":
        "Smart Code Review Agent API"

    }



@app.post("/review")
def review_code(request: ReviewRequest):


    try:

        # 输入校验
        if not request.code.strip():

            return {
                "error": "代码不能为空"
            }


        result = agent.review(
            request.code
        )


        return result


    except Exception as e:

        return {
            "error": "代码审查失败",
            "detail": str(e)
        }