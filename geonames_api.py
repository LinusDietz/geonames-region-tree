import urllib.request
from time import sleep

import xmltodict


class GeonamesAPI:
    def __init__(self, throttle: float, logging, user):
        self.base_url = 'http://api.geonames.org/'
        self.throttle = throttle
        self.logging = logging
        self.user = user

    def do_api_call(self, api: str, geoname_id: int) -> dict:
        sleep(self.throttle)
        raw_dict = xmltodict.parse(urllib.request.urlopen(self.base_url + "%s?geonameId=%s&username=%s" % (api, geoname_id, self.user)).read())

        self.log_status_message(raw_dict)
        return raw_dict

    def children(self, geoname_id: int) -> dict:
        return self.do_api_call('children', geoname_id)

    def name(self, geoname_id: int) -> dict:
        return self.do_api_call('get', geoname_id)

    def log_status_message(self, raw_dict):
        try:
            status_message = raw_dict['geonames']['status']['@message']
            if status_message.startswith('no children for'):
                self.logging.info(status_message)
            else:
                self.logging.warning(status_message)
        except KeyError:
            pass
