import logging
import os
import unittest

from geonames_api.geonames_api import GeonamesAPI
from geonames_api.model.region import Region, Coordinate
from regiontree.region_tree import RegionTree

api = GeonamesAPI(0.1, logging, os.environ['GEONAMES_KEY'])


class TestGeonamesRegionTreeAPI(unittest.TestCase):
    world_tree = RegionTree(api)

    def test_reverse_id_bavaria(self):
        bavaria = Region(2951839, 'Bavaria', 'Bavaria', Coordinate(49, 11.5))

        self.assertEqual(bavaria, self.world_tree.get_region(api.reverse_region_geoname_id(Coordinate(48.331142, 11.241698))))

    def test_reverse_id_kansas(self):
        kansas = Region(4273857, 'Kansas', 'Kansas', Coordinate(38.50029, -98.50063))
        kansas_id = api.reverse_region_geoname_id(Coordinate(38.451545, -100.428978))

        self.assertEqual(kansas, self.world_tree.get_region(kansas_id))

    def test_reverse_id_madhya_pradesh(self):
        madyha_pradesh = Region(1264542, 'Madhya Pradesh', 'Madhya Pradesh', Coordinate(23.5, 78.5))
        madyha_pradesh_id = api.reverse_region_geoname_id(Coordinate(23.5333549, 79.2399223))

        self.assertEqual(madyha_pradesh, self.world_tree.get_region(madyha_pradesh_id))
