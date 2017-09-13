import logging
import os

from regiontree.geonames_api import GeonamesAPI
from regiontree.region_tree import RegionTree

logging.basicConfig(filename='API_failures.log', format='%(asctime)s %(levelname)s: %(message)s', filemode='w', level=logging.DEBUG)

if __name__ == '__main__':
    throttle = 0.1
    geonames_user = os.environ['GEONAMES_KEY']

    world_tree = RegionTree(GeonamesAPI(throttle, logging, geonames_user))
    world_tree.print_region_tree()
    world_tree.dot_country_tree()
    world_tree.dot_continent_trees()
