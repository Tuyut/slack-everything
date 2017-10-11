# -*- coding: utf-8 -*-
import asyncio

from config import LOGGER


@asyncio.coroutine
def run_periodic_task(periodic_task):
    while True:
        periodic_task.periodic_called()
        yield from asyncio.sleep(periodic_task.get_next_exec())


class PeriodicTask(object):
    @classmethod
    def get_next_exec(cls):
        raise NotImplementedError

    @classmethod
    def periodic_called(cls):
        raise NotImplementedError
