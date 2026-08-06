"""
代码评审Agent核心模块

作用：
1. 接收用户代码
2. 判断代码语言
3. 调用对应分析工具
4. 返回检查结果
"""


# 导入Python静态检查模块
from analyzer.pylint_checker import check_python_code


# 导入Java静态检查模块
from analyzer.checkstyle_checker import check_java_code


# 导入大模型分析模块
from analyzer.llm_checker import check_by_llm


# 导入风险分析模块
from agent.risk_analyzer import (
    analyze_risk,
    get_risk_description
)

# 导入问题分析模块
from agent.issue_analyzer import analyze_issues


# 导入修复建议生成模块
from agent.fix_generator import generate_fix


# 导入日志模块
from utils.logger import logger


class CodeReviewAgent:
    """
    代码评审Agent类

    一个Agent负责：
    接收任务
    调用工具
    整合结果
    """


    def __init__(self):
        """
        初始化Agent

        这里以后可以放：
        - 模型配置
        - 工具列表
        - 参数配置
        """

        logger.info(
            "Code Review Agent 初始化完成"
        )


    def detect_language(self, code):
        """
        判断代码语言

        简单规则：
        Python:
            出现def、import

        Java:
            出现class、public、static

        """


        # 判断Java特征

        if (
            "public class" in code
            or "public static" in code
            or "System.out" in code
        ):
            return "java"



        # 判断Python特征

        elif (
            "def " in code
            or "import " in code
            or "print(" in code
        ):
            return "python"



        # 无法判断

        else:
            return "unknown"



    def review(self, code):
        """
        核心评审函数

        输入：
            用户代码

        输出：
            评审结果
        """


        # 第一步：识别语言

        language = self.detect_language(code)


        logger.info(
            f"检测到代码语言：{language}"
        )


        # 保存静态检查结果

        static_result = ""



        # Python代码

        if language == "python":

            static_result = check_python_code(code)



        # Java代码

        elif language == "java":

            static_result = check_java_code(code)



        else:

            logger.info(
                f"无法识别语言，静态检查跳过"
            )



        # 调用大模型分析

        ai_result = check_by_llm(
            code,
            static_result
        )


        # 返回最终结果

        risk = analyze_risk(
            static_result,
            ai_result
        )

        risk_description = get_risk_description(
            risk
        )

        issue_summary = analyze_issues(
            ai_result
        )

        logger.info(
            f"代码风险等级：{risk}"
        )

        fix_result = generate_fix(
            code,
            ai_result
        )
        
        return {

            "language": language,

            "risk": risk,

            "risk_description": risk_description,

            "issue_summary": issue_summary,

            "static_check": static_result,

            "ai_review": ai_result,

            "fix": fix_result
        }  