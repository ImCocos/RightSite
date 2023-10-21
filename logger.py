import logging


logger = logging.getLogger(__name__)

file_handler = logging.FileHandler(f"{__name__}.log", mode='w')
stream_handler = logging.StreamHandler()

file_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
stream_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
stream_handler.setFormatter(stream_formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
