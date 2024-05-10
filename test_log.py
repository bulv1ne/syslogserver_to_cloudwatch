import logging
from logging.handlers import SysLogHandler

logger = logging.getLogger("test_log")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
udp_handler = SysLogHandler(("127.0.0.1", 5140))
udp_handler.setFormatter(formatter)
udp_handler.setLevel(logging.DEBUG)
logger.addHandler(udp_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logger.info("Hello world")

try:
    int("tien")
except ValueError:
    logger.error("Error happened", exc_info=True)

logger.warning("Bye world")
