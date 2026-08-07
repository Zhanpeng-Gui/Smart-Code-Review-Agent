"""
Agent工具注册中心

负责管理Agent可以调用的工具
"""


class ToolRegistry:
    """
    工具注册器
    """

    def __init__(self):

        self.tools = {}


    def register(
        self,
        name,
        func
    ):

        """
        注册工具
        """

        self.tools[name] = func



    def get(
        self,
        name
    ):

        """
        获取工具
        """

        return self.tools.get(name)



    def list_tools(self):

        """
        查看所有工具
        """

        return list(
            self.tools.keys()
        )