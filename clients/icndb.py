# -*- coding: utf-8 -*-
import os
import requests

from config import LOGGER


class IcndbClient():
    __name__ = 'icndb'

    def __init__(self):
        self.endpoint = "http://api.icndb.com"
        self.failed = "Oops, something went wrong! No joke for you ;("

    def fetch_joke(self, joke_id=None):
        """Get joke from API, random if no joke_id is specified."""
        if not joke_id:
            joke = self._get('jokes/random')
        else:
            joke = self._get('jokes/%s' % str(joke_id))
        if not joke or 'joke' not in joke.keys():
            return self.failed
        return joke['joke']

    def _get(self, endpoint, params=None, headers=None):
        endpoint = os.path.join(self.endpoint, endpoint)

        response = requests.get(endpoint, params=params, headers=headers)

        if response.status_code != 200:
            LOGGER.error("%s failed: [%s] %s", self.__name__, response.status_code, response.text)
            return False

        rep = response.json()
        if rep.get('type') != 'success':
            LOGGER.error("%s failed: %s", self.__name__, rep.get('type'))
            return False
        return rep.get('value')
