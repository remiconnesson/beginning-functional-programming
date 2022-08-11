from random import random
# Non functional code

time = 5
car_positions = [1, 1, 1]

while time:
    time -= 1
    print('')
    for i in range(len(car_positions)):
        if random() > 0.3:
            car_positions[i] += 1
        print('-' * car_positions[i])

"""
This code is a car race, a `-` represents the car position.
At each time step a car may move or stall.
"""
print("new_race")

# My (functional?) solution

time = 5
car_positions = [1, 1, 1]

def move_car(position):
    return position + int(random() > 0.3)

for i in range(time):
    car_positions = list(map(move_car, car_positions))

    print('')
    for car_position in car_positions:
        print('-' * car_position)


