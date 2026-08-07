from abc import ABC, abstractmethod


class BaseTool(ABC):

    """
    Agent工具基础接口
    """

    name = ""

    description = ""


    @abstractmethod
    def run(self, code):
        pass