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
