"""
问题统计模块

作用：
统计AI发现的问题数量和等级
"""


import json



def analyze_issues(ai_result):
    """
    统计AI问题数量
    """

    result = {

        "total": 0,

        "high": 0,

        "medium": 0,

        "low": 0

    }


    try:

        data = json.loads(ai_result)


        issues = data.get(
            "issues",
            []
        )


        result["total"] = len(issues)


        for issue in issues:


            level = issue.get(
                "level",
                ""
            )


            level = level.lower()


            if (
                "error" in level
                or
                "high" in level
                or
                "严重" in level
            ):

                result["high"] += 1



            elif (
                "warning" in level
                or
                "medium" in level
                or
                "中" in level
            ):

                result["medium"] += 1



            else:

                result["low"] += 1



    except Exception:

        pass



    return result