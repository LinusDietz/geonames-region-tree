import urllib.request
from time import sleep

import xmltodict

from geonames_api.model.region import Region, Coordinate


class GeonamesAPI:
    def __init__(self, throttle: float, logging, user: str):
        self.base_url = 'http://api.geonames.org/'
        self.throttle = throttle
        self.logging = logging
        if user is None or user == '':
            raise ValueError("No geonames user provided! Set an environment variable using export GEONAMES_KEY=<user>")
        self.user = user

    def call_geonames(self, request) -> dict:
        sleep(self.throttle)
        return xmltodict.parse(urllib.request.urlopen(self.base_url + request).read())

    def do_id_api_call(self, api: str, geoname_id: int) -> dict:
        raw_dict = self.call_geonames("%s?geonameId=%s&username=%s" % (api, geoname_id, self.user))
        self.log_status_message(raw_dict)
        return raw_dict

    def children(self, geoname_id: int) -> set():
        result = set()
        try:
            raw_result = self.do_id_api_call('children', geoname_id)

            if raw_result['geonames']['totalResultsCount'] == '0':
                return result

            if raw_result['geonames']['totalResultsCount'] == '1':
                result.add(Region(int(raw_result['geonames']['geoname']['geonameId']),
                                  raw_result['geonames']['geoname']['name'],
                                  raw_result['geonames']['geoname']['toponymName'],
                                  Coordinate(raw_result['geonames']['geoname']['lat'], raw_result['geonames']['geoname']['lng'])
                                  ))
            else:
                for child in raw_result['geonames']['geoname']:
                    result.add(Region(int(child['geonameId']), child['name'], child['toponymName'], Coordinate(child['lat'], child['lng'])))

            return result
        except KeyError:
            return set()

    def name(self, geoname_id: int) -> dict:
        return self.do_id_api_call('get', geoname_id)

    def log_status_message(self, raw_dict):
        try:
            status_message = raw_dict['geonames']['status']['@message']
            if status_message.startswith('no children for'):
                self.logging.info(status_message)
            else:
                self.logging.warning(status_message)
        except KeyError:
            pass

    def reverse_region(self, point: Coordinate) -> str:

        raw_dict = self.call_geonames(f"countrySubdivision?lat={point.latitude}&lng={point.longitude}&username={self.user}")
        try:
            return raw_dict['geonames']['countrySubdivision']['adminName1']
        except KeyError:
            # Retry with country
            try:
                return raw_dict['geonames']['countrySubdivision']['countryName']
            except KeyError:
                return None

    def reverse_region_geoname_id(self, point: Coordinate) -> int:
        raw_dict = self.call_geonames(f"countrySubdivision?lat={point.latitude}&lng={point.longitude}&username={self.user}")

        try:
            return self.geoname_id_of_region(raw_dict['geonames']['countrySubdivision']['adminName1'])
        except KeyError:
            # Retry with country
            try:
                return self.geoname_id_of(raw_dict['geonames']['countrySubdivision']['countryName'])
            except KeyError:
                return 0

    def geoname_id_of_region(self, name: str, ) -> int:
        raw_dict = self.call_geonames(f"search?q={name.replace(' ', '-')}&maxRows=10&username={self.user}")
        for result in raw_dict['geonames']['geoname']:
            if result['fcl'] == 'A' and result['fcode'] == 'ADM1':
                return int(result['geonameId'])

    def geoname_id_of(self, name: str, ) -> int:
        raw_dict = self.call_geonames(f"search?q={name.replace(' ', '-')}&maxRows=1&username={self.user}")
        try:
            return int(raw_dict['geonames']['geoname']['geonameId'])
        except KeyError:
            return None
