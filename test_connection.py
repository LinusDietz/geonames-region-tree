import json
import logging

from geonames_api import GeonamesAPI
from region_tree import RegionTree

logging.basicConfig(filename='API_failures.log', format='%(asctime)s %(levelname)s: %(message)s', filemode='w', level=logging.DEBUG)


def read_config() -> dict:
    with open('config.json') as config_file:
        return json.load(config_file)


if __name__ == '__main__':
    config = read_config()
    throttle = float(config['throttle'])
    geonames_user = config['geonames_user']

    world_tree = RegionTree(GeonamesAPI(throttle, logging, geonames_user))
    world_tree.print_region_tree()
