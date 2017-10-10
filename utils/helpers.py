# -*- coding: utf-8 -*-
import logging
import sys
import yaml


def create_logger(name, level):
    """Create base logger, getting level from environement."""
    formatter = logging.Formatter("[%(asctime)s][%(levelname)s][%(name)s][%(module)s] %(message)s")
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger


def load_config(file_path):
    """Load YAML config from file path."""
    with open(file_path, 'r') as f:
        config = yaml.load(f)
    return config


def get_log_level(config):
    """Get log level to environment."""
    env = config['general']['environment']
    return config['general']['log_level'][env]
