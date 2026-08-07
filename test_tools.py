from tools.tool_manager import create_tool_registry


registry = create_tool_registry()


print(
    registry.list_tools()
)