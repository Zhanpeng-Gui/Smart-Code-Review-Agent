from tools.base_tool import BaseTool

from analyzer.llm_checker import check_by_llm



class LLMCheckerTool(BaseTool):

    name = "llm_checker"


    description = (
        "调用大语言模型分析代码问题"
    )


    def run(self, code, static_result=""):

        return check_by_llm(
            code,
            static_result
        )