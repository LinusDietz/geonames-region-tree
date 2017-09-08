# Region Tree of the World

[![Build Status](https://travis-ci.com/lynyus/geonames-region-tree.svg?token=3xSpCxqKzHnH2NXbgTwq&branch=master)](https://travis-ci.com/lynyus/geonames-region-tree)
[![Dependency Status](https://www.versioneye.com/user/projects/59a01799368b08003f17277e/badge.svg?style=flat-square)](https://www.versioneye.com/user/projects/59a01799368b08003f17277e)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d8d949fa71ee4d188f1f97b58efcfff9)](https://www.codacy.com/app/lynyus/geonames-region-tree?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lynyus/geonames-region-tree&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/d8d949fa71ee4d188f1f97b58efcfff9)](https://www.codacy.com/app/lynyus/geonames-region-tree?utm_source=github.com&utm_medium=referral&utm_content=lynyus/geonames-region-tree&utm_campaign=Badge_Coverage)

Builds a region tree using the [GeoNames API](http://www.geonames.org).

The four levels of the tree are Earth -> continents -> countries -> states.
At the time of this writing it returned 7 continents, 250 countries and 3874 federal states/sub-regions of countries.


## Usage

The usage is intended to be as a library, the main class is [`regiontree.region_tree.RegionTree`](regiontree/region_tree.py).



## License

This library is licensed under the MIT license. See the [LICENSE.md](LICENSE.md) for the full MIT license.
