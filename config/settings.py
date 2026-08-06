import os

from dotenv import load_dotenv


load_dotenv()


DASHSCOPE_API_KEY = os.getenv(
    "DASHSCOPE_API_KEY"
)


LLM_MODEL = "qwen-turbo"


LLM_BASE_URL = (
    "https://dashscope.aliyuncs.com/"
    "compatible-mode/v1"
)