import random

random_integer = random.randint(1,10)

print(random_integer)
print("Hello"[::-1])

test_seed = int(input("Enter the seed: "))
random.seed(test_seed)

namesAsCSV = input("Give me the names: ")
names = namesAsCSV.split(", ")
a = len(names)

random_pick = random.randint(0,a-1)

print(f'{names[random_pick]} will pay the bill')