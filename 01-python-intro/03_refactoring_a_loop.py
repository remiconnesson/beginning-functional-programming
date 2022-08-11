# Non functional code
people = [{'name': 'Mary', 'height':160},
          {'name': 'Isla', 'height':80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0

for person in people:
    if "height" in person:
        height_total += person["height"]
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count
    print(average_height)

# Functional Code
# ... my solution

from functools import reduce

accumulateur = {"total":0, "count":0}

def sum_and_count(acc, value):
    acc["total"] += value
    acc["count"] += 1
    return acc

people_with_heights = filter(lambda x: "height" in x, people)
accumulateur = reduce(lambda a,x : sum_and_count(a, x["height"]),
                      people_with_heights,
                      accumulateur)

if accumulateur["count"] > 0:
    average_height = accumulateur["total"] / accumulateur["count"]
    print(average_height)

"""
Note to myself:
I was trying to avoid "unrolling" the generator with `list(gen)` to get the count.
"""

# Functional Code
# ... Mary's Solution
from functools import reduce
from operator import add

people_with_heights = filter(lambda x: "height" in x, people)
heights = map(lambda x: x["height"], people_with_heights)

# Mary's Solution struggle with Python3 (it was written in python2)
heights = list(heights) # here we "unroll" the generator, I dunno if that matters or not.

if len(heights) > 0:
    total_height = reduce(add, heights, 0)
    average_height = total_height / len(list(heights))
    print(average_height)





