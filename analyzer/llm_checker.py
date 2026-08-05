from openai import OpenAI
from dotenv import load_dotenv
import os


# 加载.env文件
load_dotenv()


# 从环境变量读取key
client = OpenAI(
    api_key=os.getenv(
        "DASHSCOPE_API_KEY"
    ),

    base_url=
    "https://dashscope.aliyuncs.com/compatible-mode/v1"
)



def check_by_llm(code, static_result):


    prompt = f"""
你是一名资深后端工程师。

请审查下面代码：


代码：

{code}


静态检查结果：

{static_result}


请结合静态检查结果进行分析。

检查：

1.SQL注入风险
2.空指针风险
3.资源泄露风险
4.事务问题
5.代码设计问题

注意：
不要重复报告静态检查已经发现的问题。
重点分析静态工具无法发现的潜在风险。

请严格按照JSON格式输出：

{{
    "issues":[
        {{
            "type":"",
            "level":"",
            "location":"",
            "reason":"",
            "suggestion":""
        }}
    ]
}}
"""


    try:

        response = client.chat.completions.create(

            model="qwen-turbo",

            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]

        )


        return response.choices[0].message.content



    except Exception as e:


        return """
    {
        "issues":[
            {
                "type":"LLM Error",
                "level":"warning",
                "location":"AI service",
                "reason":"模型调用失败",
                "suggestion":"请检查网络连接或者API配置"
            }
        ]
    }
    """