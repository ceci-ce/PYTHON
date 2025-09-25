import random
import statistics

tiradas = []

for i in range(10):
    tiradas.append(random.randint(1,6))

print(f"Las tiradas han sido {tiradas}")
print(f"El primer número más repetido es {statistics.mode(tiradas)}")