"""
Agent任务规划器

负责：
1. 分析输入任务
2. 制定执行计划
"""


class Planner:


    def create_plan(
        self,
        language
    ):

        """
        根据语言生成执行计划
        """


        plan = []


        if language == "python":

            plan.append(
                "python_checker"
            )


        elif language == "java":

            plan.append(
                "java_checker"
            )


        else:

            return plan



        # 所有语言都需要AI分析

        plan.append(
            "llm_checker"
        )


        return plan