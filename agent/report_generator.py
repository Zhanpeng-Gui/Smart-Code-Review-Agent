"""
Markdown报告生成模块

作用：
把Agent结果保存成md文件
"""

from agent.report_formatter import format_ai_result

def generate_report(result):
    """
    生成Markdown格式报告

    参数:
        result:
            Agent返回的字典

    返回:
        报告文件路径
    """


    # 获取语言

    language = result["language"]

    # 获取风险等级
    risk = result["risk"]

    # 获取静态检查结果

    static_result = result["static_check"]


    # 获取AI分析结果

    ai_result = result["ai_review"]


    # 格式化AI结果
    ai_result = format_ai_result(
        ai_result
    )


    # 拼接Markdown内容

    markdown = f"""
# Code Review Report


## 一、代码语言

{language}



## 二、静态检查结果

{static_result}




## 三、AI智能分析


{ai_result}


"""


    # 保存文件

    with open(
        "review_report.md",
        "w",
        encoding="utf-8"
    ) as f:


        f.write(markdown)



    return "review_report.md"