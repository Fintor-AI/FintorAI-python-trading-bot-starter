import logging
from pathlib import Path


def init_logger(level=logging.INFO) -> logging.Logger:
    logger = logging.getLogger("fintorai_bot")

    if logger.handlers:
        return logger

    logger.setLevel(level)

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    file_handler = logging.FileHandler(log_dir / "bot.log")
    stream_handler = logging.StreamHandler()

    fmt = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler.setFormatter(fmt)
    stream_handler.setFormatter(fmt)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.info("Logger initialized.")
    return logger
