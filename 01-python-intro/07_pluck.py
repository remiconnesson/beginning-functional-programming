bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

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

"""
Create a function that extract only name and country
"""
def pluck(keys):
    def pluck_fn(record):
        return reduce(lambda a, x: assoc(a, x, record[x]),
                      keys,
                      {})
    return pluck_fn

print(list(pipeline_each(bands,
                         [set_canada_as_country,
                          strip_punctuation_from_name,
                          capitalize_names,
                          pluck(['name', 'country'])]
                         )))

