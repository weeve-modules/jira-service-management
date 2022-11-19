"""
Set up a customized logging.
"""

from os import getenv
from logging import basicConfig, DEBUG, INFO, WARNING, ERROR, CRITICAL

log_levels = {
    "DEBUG": DEBUG,
    "INFO": INFO,
    "WARNING": WARNING,
    "ERROR": ERROR,
    "CRITICAL": CRITICAL,
}


def setup_logging():
    """
    Configure logger.
    """

    log_level = (
        log_levels[getenv("LOG_LEVEL")] if getenv("LOG_LEVEL") in log_levels else INFO
    )

    basicConfig(
        level=log_level,
        format="{'level': '%(levelname)s', 'time': '%(asctime)s', 'filename': '%(name)s', 'message': '%(message)s'}",
    )
