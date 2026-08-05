"""
JSON解析工具

处理LLM返回的Markdown代码块
"""


import json



def parse_llm_json(text):
    """
    解析LLM返回JSON

    支持：

    1. 原始JSON

    2. ```json
       {}
       ```
    """


    try:

        # 去除空格

        text = text.strip()


        # 如果有markdown代码块

        if text.startswith("```"):


            text = text.replace(
                "```json",
                ""
            )


            text = text.replace(
                "```",
                ""
            )


            text = text.strip()



        return json.loads(text)



    except Exception:


        return {}