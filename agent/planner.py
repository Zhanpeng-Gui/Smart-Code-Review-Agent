"""
Agent任务规划模块

根据代码类型决定调用哪些工具
"""


from utils.logger import logger



class Planner:


    def create_plan(self, language):


        logger.info(
            f"Planner开始规划任务: {language}"
        )


        plan = {


            "language": language,


            "tools": []

        }



        if language == "python":


            plan["tools"] = [

                "python_checker",

                "llm_checker"

            ]



        elif language == "java":


            plan["tools"] = [

                "java_checker",

                "llm_checker"

            ]



        else:


            plan["tools"] = [

                "llm_checker"

            ]



        return plan