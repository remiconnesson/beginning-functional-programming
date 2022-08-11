"""
Imperative Version
"""
print("Imperative version")
bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

def format_bands(bands):
    for band in bands:
        band["country"] = 'Canada'
        band["name"] = band["name"].replace(".", '')
        band["name"] = band["name"].title()

format_bands(bands)

print(bands)

"""
Functional Version (my version)
"""
print("Functional Version")
def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

def set_canada_as_country(band):
    return assoc(band, "country", "Canada")

def strip_punctuation_from_name(band):
    return assoc(band, 'name', band['name'].replace('.', ''))

def capitalize_names(band):
    return assoc(band, 'name', band['name'].title())

bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

def pipeline_each(bands, pipeline):
    if not pipeline:
        return bands
    func, *pipeline = pipeline
    bands = map(func, bands)
    return pipeline_each(bands, pipeline)

print(list(pipeline_each(bands,
                    [set_canada_as_country,
                     strip_punctuation_from_name,
                     capitalize_names])))

"""
Functional Version (Mary's)
"""
print("Mary's version")
from functools import reduce
def pipeline_each(data, fns):
    return reduce(lambda a, x: map(x, a),
                  fns,
                  data)

def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

def call(fn, key):
    def apply_fn(record):
        return assoc(record, key, fn(record.get(key)))
    return apply_fn

set_canada_as_country = call(lambda x: 'Canada', 'country')

strip_punctuation_from_name = call(lambda x: x.replace('.', ''), 'name')

capitalize_names = call(str.title, 'name')

print(list(pipeline_each(bands,
                         [set_canada_as_country,
                          strip_punctuation_from_name,
                          capitalize_names]
                         )))


