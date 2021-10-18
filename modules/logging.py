import sys
from loguru import logger


def set_logger_setting():
    logger.remove()

    logger.add(
        sys.stdout,
        format=("".join((
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>",
            " | <lvl>{level}</lvl> | ",
            "<cyan>{message}</cyan>"
        ))),
        level="INFO",
        colorize=True,
        enqueue=True
    )

    logger.add(
        "./log/errors.log",
        format=("".join((
            "{time:YYYY-MM-DD HH:mm:ss.SSS}",
            " | {level} | ",
            "{file} (function: {function}, line: {line}) | ",
            "{message}"
        ))),
        level="ERROR",
        colorize=False,
        enqueue=True,
        rotation="10 MB",
        compression="zip"
    )
