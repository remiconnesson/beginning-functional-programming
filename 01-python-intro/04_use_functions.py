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
"""
Mary's intermediary step
"""
print('intermediary solution')
car_positions = [1, 1, 1]
def move_cars():
    for i, _ in enumerate(car_positions):
        if random() > 0.3:
            car_positions[i] += 1

def draw_car(car_position):
    print('_' * car_position)

time = 5
def run_time_step():
    global time
    time -= 1
    move_cars()

def draw():
    print('')
    for car_position in car_positions:
        draw_car(car_position)

while time:
    run_time_step()
    draw()

"""
Mary functionnal solution
"""
# Reading it I remember thinking: this look like state in JS

print("new race (func)")

def move_cars(car_positions):
    return list(map(lambda x: x + int(random() > 0.3),
               car_positions))

def output_car(car_position):
    return '-' * car_position

def run_step_of_race(state):
    return {'time': state['time'] - 1,
            'car_positions': move_cars(state['car_positions'])}

def draw(state):
    print('')
    lines = '\n'.join(map(output_car, state['car_positions']))
    print(lines)

def race(state):
    draw(state)
    if state['time']:
        race(run_step_of_race(state))

race({
        'time': 5,
        'car_positions': [1, 1, 1],
    })
