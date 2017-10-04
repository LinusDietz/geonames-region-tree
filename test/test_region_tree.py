import difflib
import logging
import os
import unittest

from geonames_api.geonames_api import GeonamesAPI
from regiontree.region_tree import RegionTree


class TestRegionTree(unittest.TestCase):
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)
    world_tree = RegionTree(GeonamesAPI(0.1, logging, os.environ['GEONAMES_KEY']))

    def test_number_of_continents(self):
        self.assertEqual(7, len(self.world_tree.tree))

    def test_get_countries(self):
        self.assertEqual(250, len(self.world_tree.get_countries()))

    def test_number_of_regions(self):
        expected_num_states = 3874
        num_states = 0
        for continent in self.world_tree.tree:
            for country in continent:
                num_states += len(country)

        self.assertEqual(expected_num_states, num_states)

    def test_region_info(self):
        self.world_tree.print_region_tree('./resources/world_tree_new.txt')
        with open('./resources/world_tree.txt', 'r', encoding="utf-8") as old:
            with open('./resources/world_tree_new.txt', 'r', encoding="utf-8") as new:
                print(''.join(difflib.ndiff(sorted([l.strip() + '\n' for l in old.readlines()]), sorted([l.strip() + '\n' for l in new.readlines()]))))
