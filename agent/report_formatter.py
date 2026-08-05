"""
报告格式化模块

作用：
把AI返回JSON转换成Markdown表格
"""


from utils.json_parser import parse_llm_json



def convert_level(level):
    """
    AI等级转中文
    """

    level = level.lower()


    if level in [
        "error",
        "high",
        "critical"
    ]:
        return "严重"



    elif level in [
        "warning",
        "medium",
    ]:
        return "警告"



    else:
        return "提示"





def format_ai_result(ai_result):
    """
    JSON转Markdown
    """


    data = parse_llm_json(
        ai_result
    )


    issues = data.get(
        "issues",
        []
    )


    if not issues:

        return "没有发现明显问题"



    markdown = """
|类型|等级|位置|原因|修改建议|
|-|-|-|-|-|
"""


    for issue in issues:


        markdown += (
            f"|{issue.get('type')}|"
            f"{convert_level(issue.get('level',''))}|"
            f"{issue.get('location','')}|"
            f"{issue.get('reason','')}|"
            f"{issue.get('suggestion','')}|\n"
        )



    return markdown