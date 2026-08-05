"""
问题统计模块

作用：
统计AI发现的问题数量和等级
"""


from utils.json_parser import parse_llm_json



def analyze_issues(ai_result):
    """
    统计AI问题数量

    返回:

    {
        total: 总数量,
        high: 严重数量,
        medium: 警告数量,
        low: 提示数量
    }

    """



    result = {

        "total": 0,

        "high": 0,

        "medium": 0,

        "low": 0

    }



    try:


        # =========================
        # 解析AI JSON
        # =========================


        data = parse_llm_json(
            ai_result
        )



        issues = data.get(
            "issues",
            []
        )



        # 问题总数

        result["total"] = len(
            issues
        )



        # =========================
        # 分析等级
        # =========================

        for issue in issues:


            level = issue.get(
                "level",
                ""
            )


            level = level.lower()



            # 严重

            if (

                "error" in level

                or

                "high" in level

                or

                "critical" in level

                or

                "严重" in level

            ):


                result["high"] += 1



            # 警告

            elif (

                "warning" in level

                or

                "warn" in level

                or

                "medium" in level

                or

                "中" in level

                or

                "警告" in level

            ):


                result["medium"] += 1



            # 提示

            else:


                result["low"] += 1




    except Exception as e:


        print(
            "问题统计失败:",
            e
        )



    return result