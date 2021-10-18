import sys
from loguru import logger


def set_logger_setting():
    logger.remove()

    logger.add(
        sys.stdout,
        format=(str().join([
            "<lvl>{level}</lvl>",
            " | <green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | ",
            "<cyan>{message}</cyan>"
        ])),
        level="INFO",
        colorize=True,
        enqueue=True
    )

    logger.add(
        "./log/errors.log",
        format=(str().join([
            "{level}",
            " | {time:YYYY-MM-DD HH:mm:ss.SSS} | ",
            "{file} (function: {function}, line: {line}) | ",
            "{message}"
        ])),
        level="ERROR",
        colorize=False,
        enqueue=True
    )
