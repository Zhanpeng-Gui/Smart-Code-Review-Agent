"""
报告格式化模块

作用：
把AI返回JSON转换成Markdown表格
"""


import json



def format_ai_result(ai_result):
    """
    将AI JSON结果转换成Markdown表格
    """


    try:

        # 字符串转JSON

        data = json.loads(ai_result)


    except Exception:


        return ai_result



    issues = data.get(
        "issues",
        []
    )


    if not issues:

        return "没有发现明显问题"



    markdown = """|类型|等级|位置|原因|修改建议|\n|-|-|-|-|-|\n"""



    for issue in issues:


        markdown += (
            f"|{issue.get('type')}|"
            f"{issue.get('level')}|"
            f"{issue.get('location')}|"
            f"{issue.get('reason')}|"
            f"{issue.get('suggestion')}|\n"
        )




    return markdown