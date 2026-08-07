from tools.registry import ToolRegistry

from tools.python_tool import PythonCheckerTool
from tools.java_tool import JavaCheckerTool
from tools.llm_tool import LLMCheckerTool



def create_tool_registry():

    registry = ToolRegistry()


    registry.register(
        PythonCheckerTool()
    )


    registry.register(
        JavaCheckerTool()
    )


    registry.register(
        LLMCheckerTool()
    )


    return registry