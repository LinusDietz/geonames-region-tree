import logging
import os
import unittest

from regiontree.geonames_api import GeonamesAPI
from regiontree.region import Coordinate

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)

api = GeonamesAPI(1, logging, os.environ['GEONAMES_KEY'])


class TestGeocodeAPI(unittest.TestCase):
    def test_reverse_tyrol(self):
        self.assertEqual('Tyrol', api.reverse_region(Coordinate(47.0, 10.2)))

    def test_reverse_pacific_ocean(self):
        self.assertIsNone(api.reverse_region(Coordinate(33, 167)))

    def test_reverse_berlin(self):
        self.assertEqual('Berlin', api.reverse_region(Coordinate(52.521834, 13.413179)))

    def test_reverse_bavaria(self):
        self.assertEqual('Bavaria', api.reverse_region(Coordinate(48.262844, 11.668678)))

    def test_reverse_antarctica(self):
        self.assertEqual('Antarctica', api.reverse_region(Coordinate(-76.472862, 28.370260)))

    def test_reverse_arctic(self):
        self.assertIsNone(api.reverse_region(Coordinate(90, 0)))

    def test_get_id_bavaria(self):
        self.assertEqual(2951839, api.geoname_id_of('Bavaria'))

    def test_get_id_unknown(self):
        self.assertIsNone(api.geoname_id_of('WhateverNonexistentCountry'))

    def test_get_id_papua_new_guinea(self):
        self.assertEqual(2088628, api.geoname_id_of('Papua New Guinea'))
