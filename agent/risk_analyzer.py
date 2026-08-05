"""
风险等级分析模块

根据AI分析结果和静态检查结果
综合判断代码风险
"""


from utils.json_parser import parse_llm_json



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


    risk = "Low"


    try:


        data = parse_llm_json(
            ai_result
        )


        issues = data.get(
            "issues",
            []
        )


        for issue in issues:


            level = issue.get(
                "level",
                ""
            ).lower()



            if level in [
                "critical",
                "error",
                "high"
            ]:

                return "High"



            elif level in [
                "warning",
                "medium",
                "warn"
            ]:

                risk = "Medium"



    except Exception as e:

        print(
            "风险分析失败:",
            e
        )



    return risk