import logging
import os


if not os.path.exists("logs"):
    os.makedirs("logs")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(
            "logs/app.log",
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ]
)


# 屏蔽第三方库日志
logging.getLogger("httpx").setLevel(
    logging.WARNING
)

logging.getLogger("openai").setLevel(
    logging.WARNING
)


logger = logging.getLogger(__name__)