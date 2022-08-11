from functools import reduce

"""
Reduce arguments
"""

initial_value_of_accumulator = 0
sum_from_0_to_4 = reduce(lambda accumulator, current_item : accumulator + current_item,
             list(range(5)),
                         initial_value_of_accumulator)

print(sum_from_0_to_4)

# equivalent to 
sum_from_0_to_4 = reduce(lambda a, x : a + x,
                         list(range(5)))

print(sum_from_0_to_4)

"""
Count Occurences of a word in a Sentences
"""
# Not functional
sentences = ["Mary read a story to Sam and Isla.",
             "Isla cuddled Same.",
             "Sam chortled."]
sam_count = 0
for sentence in sentences:
    sam_count += sentence.count("Sam")

print(sam_count)

# Functional
sentences = ["Mary read a story to Sam and Isla.",
             "Isla cuddled Same.",
             "Sam chortled."]

sam_count = reduce(lambda a, x: a + x.count("Sam"),
                   sentences,
                   0)

print(sam_count)
