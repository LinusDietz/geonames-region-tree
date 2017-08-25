class Coordinate:
    def __init__(self, lat: str, lng: str):
        self.latitude = lat
        self.longitude = lng


class Region:
    def __init__(self, geoname_id: int, name: str, toponym_name: str, position: Coordinate):
        self.children = set()
        self.geoname_id = geoname_id
        self.name = name
        self.toponym_name = toponym_name
        self.position = position

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Region #%d: %s (%s) at (%s, %s) " % (self.geoname_id, self.name, self.toponym_name, self.position.latitude, self.position.longitude)

    def add_children(self, region):
        self.children.add(region)

    def __iter__(self):
        return iter(self.children)

    def __len__(self):
        return len(self.children)
