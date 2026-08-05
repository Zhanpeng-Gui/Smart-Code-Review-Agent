"""
Markdown报告生成模块

作用：
把Agent结果保存成md文件
"""

from agent.report_formatter import format_ai_result

from agent.risk_analyzer import (
    analyze_risk,
    get_risk_description
)

def generate_report(result):
    """
    生成Markdown格式报告

    参数:
        result:
            Agent返回的字典

    返回:
        报告文件路径
    """

    issue_summary = result["issue_summary"]

    # 获取语言

    language = result["language"]

    # 获取风险等级
    risk = result["risk"]

    #增加风险描述
    risk_description = result["risk_description"]


    # 获取静态检查结果

    static_result = result["static_check"]


    # 获取AI分析结果

    ai_result = result["ai_review"]

    # 获取修复建议
    fix_result = result["fix"]

    # 格式化AI结果
    ai_result = format_ai_result(
        ai_result
    )


    # 拼接Markdown内容

    markdown = f"""
# Code Review Report


## 一、总体风险

**{risk}**

{risk_description}


## 二、问题统计

|等级|数量|
|-|-|
|严重|{issue_summary["high"]}|
|警告|{issue_summary["medium"]}|
|提示|{issue_summary["low"]}|


## 三、代码语言

{language}



## 四、AI智能分析

{ai_result}



## 五、静态检查结果

{static_result}


## 六、修复建议

{fix_result}


"""


    # 保存文件

    with open(
        "review_report.md",
        "w",
        encoding="utf-8"
    ) as f:


        f.write(markdown)



    return "review_report.md"