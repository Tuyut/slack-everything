# -*- coding: utf-8 -*-
from utils import load_config, create_logger, get_log_level

CONFIG = load_config('config/config.yml')
LOGGER = create_logger('slack-everything', get_log_level(CONFIG))
