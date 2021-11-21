import logging
logger = logging.getLogger(__name__)
logger.info('mylogger')

# Create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("log/mylog.log")

# level and format
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s:%(levelname)s:%(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning("Oops, file not found")
logger.error("This is error message, File not found")

