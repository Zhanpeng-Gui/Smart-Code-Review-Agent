"""
FastAPI接口服务

作用：
提供代码审查API
"""


from fastapi import FastAPI, HTTPException


from agent.code_review_agent import CodeReviewAgent


from pydantic import BaseModel


from typing import Any


class APIResponse(BaseModel):

    success: bool

    message: str

    data: Any = None

class ReviewRequest(BaseModel):

    code: str
    """
    待审查的源代码
    """

    language: str = "python"
    """
    编程语言
    """

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



@app.post(
    "/review",
    summary="智能代码审查接口",
    description="""
    输入源代码，
    自动完成：

    1. 代码语言检测
    2. 静态代码检查
    3. AI智能分析
    4. 风险等级评估
    5. 自动生成修复建议

    支持：
    - Python
    - Java
    """
)
def review_code(request: ReviewRequest):


    try:

        if not request.code.strip():

            raise HTTPException(
                status_code=400,
                detail="代码不能为空"
            )


        result = agent.review(
            request.code
        )


        return APIResponse(
            success=True,
            message="代码审查完成",
            data=result
        )


    except HTTPException:

        raise


    except Exception as e:

        return {
            "success": False,
            "message": f"代码审查失败: {str(e)}",
            "data": None
        }