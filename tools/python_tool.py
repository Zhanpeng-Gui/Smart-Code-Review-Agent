from tools.base_tool import BaseTool

from analyzer.pylint_checker import check_python_code



class PythonCheckerTool(BaseTool):

    name = "python_checker"


    description = (
        "使用 pylint 对 Python代码进行静态检查"
    )


    def run(self, code):

        return check_python_code(code)