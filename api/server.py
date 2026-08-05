"""
FastAPI接口服务

作用：
提供代码审查API
"""


from fastapi import FastAPI


from agent.code_review_agent import CodeReviewAgent



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
def review_code(code: str):

    """
    接收代码
    返回审查结果
    """


    result = agent.review(
        code
    )


    return result