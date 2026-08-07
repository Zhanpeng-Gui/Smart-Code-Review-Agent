from tools.base_tool import BaseTool

from analyzer.checkstyle_checker import check_java_code



class JavaCheckerTool(BaseTool):

    name = "java_checker"


    description = (
        "使用 Checkstyle 对 Java代码进行静态检查"
    )


    def run(self, code):

        return check_java_code(code)