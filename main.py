# -*- coding: utf-8 -*-
import asyncio

from config import LOGGER
from plugins import get_periodic_tasks


def run():
    """Start event loop, and run forever."""
    # Create main event loop
    event_loop = asyncio.get_event_loop()

    # Define all backgroung tasks and start them
    tasks = get_periodic_tasks()
    LOGGER.info('Adding %s periodic tasks', len(tasks))
    event_loop.run_until_complete(asyncio.wait(tasks))

    # Launch main loop
    LOGGER.info('Launching loop')
    try:
        event_loop.run_forever()
    except KeyboardInterrupt:
        LOGGER.error('Loop stopped by user')
        event_loop.close()


if __name__ == '__main__':
    run()
