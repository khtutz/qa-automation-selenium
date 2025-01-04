import logging
from logging import Logger
from datetime import datetime

from src.travel_airbnb.utils.config_reader import ConfigReader

def get_logger(name: str) -> Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:  # Avoid adding handlers multiple times
        # File handler 
        log_file = f'src/travel_airbnb/logs/log_file_{datetime.now().strftime("%Y-%m-%d")}.log'
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)

        # Stream handler for pytest capture
        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter('%(levelname)s : %(message)s')
        stream_handler.setFormatter(stream_formatter)
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        # Set log level
        config = ConfigReader()
        logger.setLevel(getattr(logging, config.log_level.upper(), logging.DEBUG))
    return logger
