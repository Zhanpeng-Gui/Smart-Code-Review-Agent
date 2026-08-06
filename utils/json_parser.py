"""
JSON解析工具

作用：
解析大模型返回的JSON
处理Markdown代码块
"""


import json
from utils.logger import logger


def parse_llm_json(text):
    """
    解析LLM返回结果

    支持：

    1. 普通JSON

    2. ```json代码块

    """


    try:


        # 去除markdown代码块


        text = text.replace(
            "```json",
            ""
        )


        text = text.replace(
            "```",
            ""
        )


        text = text.strip()



        return json.loads(
            text
        )



    except Exception as e:


        logger.error(
            f"JSON解析失败:{e}"
        )


        return {}