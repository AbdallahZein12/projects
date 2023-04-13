import logging
from logging import FileHandler
from datetime import datetime

logger = logging.getLogger(__name__)
logger.info("Hello from helper!")

file_h = logging.FileHandler(f"D:\Code\project\QRCode_Generator\logs\log.log")

file_h.setLevel(logging.ERROR)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_h.setFormatter(formatter)

logger.addHandler(file_h)



