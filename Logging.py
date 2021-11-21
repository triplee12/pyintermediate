import logging
import logging.config
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import time
import traceback


logging.config.fileConfig("log/logging.conf")

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
from log import mylogger

__author__ = "Ejie Emmanuel Ebuka"

# Logging

"""
Logging: python already makes it possible for you to quickly log your application.
We have five(5) different logs
"""
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


print("_" * 80)

logger = logging.getLogger("simpleExample")
logger.debug("This is debug message from logging.conf")

# Traceback
try:
    ab = [1, 2, 3, 4, 5]
    ind = ab[7]
except IndexError as e:
    logging.error(e, exc_info=True)

# Incase we don't know the error message

try:
    ab = [1, 2, 3, 4, 5]
    ind = ab[7]
except:
    logging.error("The error message is %s", traceback.format_exc())

# Rotating file handler
logger_f = logging.getLogger(__name__)
logger_f.setLevel(logging.INFO)

# Roll over after 5KB, and keep backup logs mylog.log.1, mylog.log.2, etc.
handler = RotatingFileHandler("log/mylog1.log", maxBytes=5000, backupCount=5)
logger_f.addHandler(handler)

for _ in range(10000):
    logger_f.info("Smiles, Hello World")

# Your application might run for a long time, you can use 'TimedRotatingFileHandler'
# This would create a log base on how much time it takes to run the application.

handler_2 = TimedRotatingFileHandler("log/timelog.log", when='s', interval=1, backupCount=5)
logger_f.addHandler(handler_2)

for _ in range(10):
    logger_f.info("Smiles, Hello World")
    time.sleep(1)

# You can use python_json_logger by simply install it
