import os
import logging
import logging.handlers

from settings.path import LOG_ROOT

LOGGING_STRING_FORMAT = (
    "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s"
)
LOG_FILE = os.path.join(LOG_ROOT, 'debug.log')
logFormatter = logging.Formatter(LOGGING_STRING_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fileHandler = logging.handlers.RotatingFileHandler(
    LOG_FILE,
    mode='a',
    maxBytes=5 * 1024 * 1024,
    backupCount=100,
    encoding=None,
    delay=0,
)
fileHandler.setFormatter(logFormatter)
fileHandler.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
consoleHandler.setLevel(logging.INFO)
logger.addHandler(consoleHandler)
