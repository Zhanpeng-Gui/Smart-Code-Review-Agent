"""
风险等级分析模块

根据AI分析结果和静态检查结果
综合判断代码风险
"""


import json



def get_risk_description(risk):
    """
    根据风险等级生成描述
    """


    if risk == "High":

        return "发现严重代码问题，建议修改后再提交。"



    elif risk == "Medium":

        return "存在潜在风险，建议人工复查。"



    else:

        return "未发现明显风险，可以继续提交。"


def analyze_risk(static_result, ai_result):
    """
    综合分析风险等级
    """



    # 默认风险

    risk = "Low"



    # =========================
    # 第一优先级：分析AI结果
    # =========================


    try:

        data = json.loads(ai_result)


        issues = data.get(
            "issues",
            []
        )


        for issue in issues:


            level = issue.get(
                "level",
                ""
            )


            level = level.lower()



            if (
                "high" in level
                or
                "严重" in level
                or
                "critical" in level
                or
                "error" in level
            ):

                return "High"



            elif (
                "medium" in level
                or
                "warning" in level
                or
                "中" in level
            ):

                risk = "Medium"



    except Exception:

        pass



    # =========================
    # 第二优先级：静态检查兜底
    # =========================


    text = static_result.lower()



    if (
        "error"
        in text
    ):

        return "High"



    if (
        "warning"
        in text
    ):

        risk = "Medium"



    return risk