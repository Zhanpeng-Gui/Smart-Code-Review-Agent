from tools.tool_manager import create_tool_registry


registry=create_tool_registry()


tool=registry.get(
    "python_checker"
)


print(type(tool))


print(
    hasattr(tool,"run")
)