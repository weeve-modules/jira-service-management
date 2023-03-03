"""
Set up a customized logging.
"""

from os import getenv
import logging
import json


# Create a JSON formatter
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "filename": record.filename,
            "message": record.getMessage(),
        }
        return json.dumps(log_data)


log_levels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


def setup_logging():
    """
    Configure logger.
    """

    log_level = (
        log_levels[getenv("LOG_LEVEL")]
        if getenv("LOG_LEVEL") in log_levels
        else logging.INFO
    )

    logHandler = logging.StreamHandler()
    logHandler.setFormatter(JSONFormatter())

    logging.basicConfig(
        level=log_level,
        handlers=[logHandler],
    )
