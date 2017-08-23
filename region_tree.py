from geonames_api import GeonamesAPI


class Region:
    def __init__(self, geoname_id: int, name: str, toponym_name: str):
        self.geoname_id = geoname_id
        self.name = name
        self.toponym_name = toponym_name

    def __str__(self):
        return self.name


EARTH = Region(6295630, 'Earth', 'Earth')


class RegionTree:
    def __init__(self, api: GeonamesAPI):
        self.api = api
        self.tree = self.build_world_tree()

    def get_children(self, region: Region = EARTH) -> set:
        result = set()
        raw_result = self.api.children(region.geoname_id)

        try:
            if raw_result['geonames']['totalResultsCount'] == '1':
                result.add(Region(raw_result['geonames']['geoname']['geonameId'], raw_result['geonames']['geoname']['name'],
                                  raw_result['geonames']['geoname']['toponymName']))
            else:
                for child in raw_result['geonames']['geoname']:
                    result.add(Region(child['geonameId'], child['name'], child['toponymName']))
        except KeyError:
            pass
        return result

    def get_countries(self) -> list():
        countries_of_the_world = list()
        for continent in self.get_children():
            [countries_of_the_world.append(country) for country in self.get_children(continent)]
        return countries_of_the_world

    def get_element(self, geoname_id: int) -> str:
        raw_result = self.api.name(geoname_id)
        return raw_result['geoname']['name']

    def build_world_tree(self) -> dict:
        region_tree = dict()
        region_tree[EARTH] = dict()
        for continent in self.get_children():
            region_tree[EARTH][continent] = dict()
            for country in self.get_children(continent):
                region_tree[EARTH][continent][country] = dict()
                for state in self.get_children(country):
                    region_tree[EARTH][continent][country][state] = set()

        return region_tree

    def print_region_tree(self):
        number_countries: int = 0
        number_states: int = 0
        with open('worldtree.txt', 'w', 1, "UTF-8", 'strict') as tree_file:
            for earth in self.tree:
                print(earth, file=tree_file)
                for continent in self.tree[earth]:
                    print("   ", continent, file=tree_file)
                    for country in self.tree[earth][continent]:
                        print("       ", country, file=tree_file)
                        number_countries += 1
                        for state in self.tree[earth][continent][country]:
                            print("           ", state, file=tree_file)
                            number_states += 1
            print('Num countries : %d, Num states: %d' % (number_countries, number_states), file=tree_file)
