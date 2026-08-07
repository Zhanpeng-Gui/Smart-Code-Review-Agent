"""
工具管理模块

负责初始化Agent工具
"""


from tools.tool_registry import ToolRegistry


from analyzer.pylint_checker import check_python_code

from analyzer.checkstyle_checker import check_java_code

from analyzer.llm_checker import check_by_llm



def create_tool_registry():

    """
    创建工具列表
    """


    registry = ToolRegistry()



    registry.register(
        "python_checker",
        check_python_code
    )


    registry.register(
        "java_checker",
        check_java_code
    )


    registry.register(
        "llm_checker",
        check_by_llm
    )


    return registry