import random

# This code is not functional
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)
print(names)


# This code is functional
names = ['Mary', 'Isla', 'Sam']

secret_names = map(lambda x : random.choice(['Mr. Pink', 'Mr. Orange', "Mr. Blonde"]),
                   names)

print(list(secret_names))

# This code is not functional
names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print(names)

# This code is functional
names = ['Mary', 'Isla', 'Sam']

secret_names = map(hash, names)

print(list(secret_names))
