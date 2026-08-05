"""
代码修复建议模块

作用：
根据代码问题生成修复建议
"""


from analyzer.llm_checker import client



def generate_fix(code, issues):
    """
    根据问题生成修复方案
    """


    prompt = f"""

你是一名资深后端工程师。

请根据下面的问题，
给出代码修复建议。


原始代码：

{code}


发现的问题：

{issues}


请输出：

1.问题原因
2.修改方案
3.修复后的代码


要求：
使用Markdown格式。


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