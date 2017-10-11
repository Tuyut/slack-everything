# -*- coding: utf-8 -*-

from config import LOGGER
from clients import IcndbClient
from tasks import PeriodicTask, PunctualTask


class Joker(PeriodicTask, PunctualTask):
    """
    Fetch random jokes from icndb API.

    periodic: fetch joke every morning
    punctual: fetch joke when called
    """
    __name__ = 'joker'

    @classmethod
    def periodic_called(cls):
        client = IcndbClient()
        joke = client.fetch_joke()

    @classmethod
    def get_next_exec(cls):
        return 86400
