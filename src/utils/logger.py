from loguru import logger

def init_logger(level="INFO"):
    logger.remove()
    logger.add(
        "bot.log",
        rotation="1 day",
        retention="7 days",
        level=level
    )
    logger.info("Logger initialized.")
