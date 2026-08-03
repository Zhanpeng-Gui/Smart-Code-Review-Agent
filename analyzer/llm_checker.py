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
1.SQL注入
2.空指针
3.资源泄露
4.事务问题
5.设计问题

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