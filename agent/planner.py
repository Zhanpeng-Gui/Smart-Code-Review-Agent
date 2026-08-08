"""
Agent任务规划模块

根据代码类型决定调用哪些工具
"""


from utils.logger import logger



class Planner:


    def create_plan(
        self,
        language,
        history=None
    ):


        print("Planner收到历史记录:")
        print(history)



        if language == "python":

            tools = [
                "python_checker",
                "llm_checker"
            ]


        elif language == "java":

            tools = [
                "java_checker",
                "llm_checker"
            ]


        else:

            tools = [
                "llm_checker"
            ]



        plan = {

            "language": language,

            "tools": tools,

            "history": history

        }


        return plan