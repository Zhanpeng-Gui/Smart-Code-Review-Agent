"""
风险等级分析模块

根据静态检查和AI结果
判断代码风险等级
"""


def analyze_risk(static_result, ai_result):
    """
    分析代码风险

    返回:
    High
    Medium
    Low
    """

    # 默认低风险

    risk = "Low"



    # 转小写方便判断

    text = (
        static_result
        +
        ai_result
    ).lower()



    # 高风险关键词

    high_keywords = [

        "sql injection",

        "sql注入",

        "nullpointer",

        "空指针",

        "undefined variable"

    ]



    # 中风险关键词

    medium_keywords = [

        "warning",

        "missing",

        "docstring"

    ]



    # 判断高风险

    for word in high_keywords:

        if word in text:

            risk = "High"

            break



    # 如果不是高风险，再判断中风险

    if risk == "Low":

        for word in medium_keywords:

            if word in text:

                risk = "Medium"

                break



    return risk