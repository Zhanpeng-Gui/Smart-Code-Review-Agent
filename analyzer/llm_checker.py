from openai import OpenAI
from config.settings import (
    DASHSCOPE_API_KEY,
    LLM_MODEL,
    LLM_BASE_URL
)



# 从环境变量读取key
client = OpenAI(

    api_key=DASHSCOPE_API_KEY,

    base_url=LLM_BASE_URL

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

请重点检查：

1.SQL注入
2.空指针
3.资源泄露
4.事务问题
5.代码设计问题


要求：

- 只返回真实存在的问题
- 不要输出不存在的问题
- 如果没有发现问题，issues返回空数组


注意：

如果代码不存在某类问题，
不要认为是风险。

例如：
没有数据库操作，
SQL注入风险等级应该为 info。

风险等级只能使用：

critical
warning
info


定义：

critical:
严重安全漏洞或运行错误

warning:
潜在问题，需要修改

info:
没有发现问题，仅说明情况

注意：
请结合静态检查结果进一步分析。

如果静态检查发现问题：
1. 解释问题影响
2. 判断风险等级
3. 给出修复方案

不要只复制静态检查文本。

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

            model=LLM_MODEL,

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