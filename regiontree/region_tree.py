from regiontree.geonames_api import GeonamesAPI
from regiontree.region import Region, Coordinate

EARTH = Region(6295630, 'Earth', 'Earth', Coordinate("0", "0"))


class RegionTree:
    def __init__(self, api: GeonamesAPI):
        self.api = api
        self.tree = self.build_world_tree()

    def get_children(self, region: Region = EARTH) -> set():

        return self.api.children(region.geoname_id)

    def get_countries(self) -> list():
        countries_of_the_world = list()
        for continent in self.get_children():
            [countries_of_the_world.append(country) for country in self.get_children(continent)]
        return countries_of_the_world

    def get_element(self, geoname_id: int) -> str:
        raw_result = self.api.name(geoname_id)
        return raw_result['geoname']['name']

    def build_world_tree(self) -> Region:
        region_tree = EARTH
        for continent in self.get_children():
            region_tree.add_children(continent)
            for country in self.get_children(continent):
                continent.add_children(country)
                for state in self.get_children(country):
                    country.add_children(state)
        return EARTH

    def print_region_tree(self, out_file='worldtree.txt'):
        number_countries: int = 0
        number_states: int = 0
        with open(out_file, 'w', 1, "UTF-8", 'strict') as tree_file:
            print(self.tree, file=tree_file)
            indent = "  "
            for continent in self.tree:
                level = 1
                print(level * indent + str(continent), file=tree_file)
                for country in continent:
                    level = 2
                    print(level * indent + str(country), file=tree_file)
                    number_countries += 1
                    for state in country:
                        level = 3
                        print(level * indent + str(state), file=tree_file)
                        number_states += 1

            print('Num countries : %d, num states: %d' % (number_countries, number_states), file=tree_file)