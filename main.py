# -*- coding: utf-8 -*-
import asyncio

from config import LOGGER


def run():
    """Start event loop, and run forever."""
    # Create main event loop
    event_loop = asyncio.get_event_loop()

    # Launch main loop
    LOGGER.info('Launching loop')
    try:
        event_loop.run_forever()
    except KeyboardInterrupt:
        LOGGER.error('Loop stopped by user')
        event_loop.close()


if __name__ == '__main__':
    run()
