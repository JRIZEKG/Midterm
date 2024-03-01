import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

for index in range(len(random_numbers)):
    if random_numbers[index] > 80:
        random_numbers[index] = -random_numbers[index]

print("Random numbers after replacing > 80 with negatives:")
print(random_numbers)