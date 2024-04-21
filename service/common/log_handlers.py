"""
Log Handlers

This module contains utility functions to set up logging consistently.
"""
import logging


def init_logging(app, logger_name: str):
    """Set up logging for production"""
    app.logger.propagate = False
    gunicorn_logger = logging.getLogger(logger_name)
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    # Define the format for logging
    log_format = ("[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s")
    date_format = "%Y-%m-%d %H:%M:%S %z"

    # Make all log formats consistent
    formatter = logging.Formatter(log_format, date_format)

    for handler in app.logger.handlers:
        handler.setFormatter(formatter)

    app.logger.info("Logging handler established")
