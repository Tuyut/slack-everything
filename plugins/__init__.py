import asyncio

from tasks import PeriodicTask, PunctualTask, run_periodic_task
from .joker import Joker

ALL_PLUGINS = [Joker]


def get_periodic_tasks():
    return [asyncio.ensure_future(run_periodic_task(plugin)) for plugin in ALL_PLUGINS
            if issubclass(plugin, PeriodicTask)]
