"""
日志模块

作用：
统一管理项目日志
"""

import logging
import os


# 获取项目根目录
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# 日志目录
LOG_DIR = os.path.join(
    BASE_DIR,
    "logs"
)


# 不存在则创建
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


LOG_FILE = os.path.join(
    LOG_DIR,
    "app.log"
)



logging.basicConfig(

    level=logging.INFO,

    format=(
        "%(asctime)s "
        "- %(levelname)s "
        "- %(message)s"
    ),

    handlers=[

        logging.FileHandler(
            LOG_FILE,
            encoding="utf-8"
        ),

        logging.StreamHandler()

    ]

)


# 关闭第三方库日志
logging.getLogger("httpx").setLevel(
    logging.WARNING
)

logging.getLogger("openai").setLevel(
    logging.WARNING
)


logger = logging.getLogger(__name__)