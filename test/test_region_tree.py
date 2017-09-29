import logging
import os
import unittest

from geonames_api.geonames_api import GeonamesAPI
from regiontree.region_tree import RegionTree


class TestRegionTree(unittest.TestCase):
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)
    world_tree = RegionTree(GeonamesAPI(0.1, logging, os.environ['GEONAMES_KEY']))

    def test_number_of_regions(self):
        expected_num_continents = 7
        expected_num_countries = 250
        expected_num_states = 3874
        num_countries = 0
        num_states = 0
        for continent in self.world_tree.tree:
            for country in continent:
                num_countries += 1
                num_states += len(country)

        self.assertEqual(expected_num_continents, len(self.world_tree.tree))
        self.assertEqual(expected_num_countries, num_countries)
        self.assertEqual(expected_num_states, num_states)

    def test_get_countries(self):
        self.assertEqual(250, len(self.world_tree.get_countries()))
