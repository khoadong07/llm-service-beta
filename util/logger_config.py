from loguru import logger

def configure_logger():
    logger.remove()
    logger.add("logs/api.log", rotation="1 week", retention="1 month", level="INFO", backtrace=True, diagnose=True)
