import logging
import os
import unittest

from regiontree.geonames_api import GeonamesAPI
from regiontree.region_tree import RegionTree

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)


class TestRegionTree(unittest.TestCase):
    def test_number_of_regions(self):
        geonames_user = os.environ['GEONAMES_KEY']

        world_tree = RegionTree(GeonamesAPI(0.0001, logging, geonames_user))

        expected_num_continents = 7
        expected_num_countries = 250
        expected_num_regions = 3874
        num_countries = 0
        num_regions = 0
        for continent in world_tree.tree:
            for country in continent:
                num_countries += 1
                num_regions += len(country)

        self.assertEqual(expected_num_continents, len(world_tree.tree))
        self.assertEqual(expected_num_countries, num_countries)
        self.assertEqual(expected_num_regions, num_regions)
