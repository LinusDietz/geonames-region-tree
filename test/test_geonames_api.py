import logging
import os
import unittest

from geonames_api.geonames_api import GeonamesAPI
from geonames_api.model.coordinate import Coordinate

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)

api = GeonamesAPI(0.1, logging, os.environ['GEONAMES_KEY'])


class TestGeonamesAPI(unittest.TestCase):
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

    def test_get_state_kansas(self):
        self.assertEqual(4273857, api.reverse_region_geoname_id(Coordinate(38.451545, -100.428978)))
