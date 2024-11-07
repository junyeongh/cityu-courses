import numpy as np
import random

p = 9001
d = 300
k = 2

a = np.zeros(k)
b = np.zeros(k)
# randomly choosing k hash functions
for i in range(k):
    a[i] = random.randint(0, p - 1)
    b[i] = random.randint(0, p - 1)

counters = np.zeros((k, d))
m = 0

for file_index in range(100):
    file_path = "data_stream/stream" + str(file_index) + ".txt"
    f = open(file_path, "r")
    for line in f.readlines():
        line = line[:-1]  # remove '\n'
        x = int(line)
        # count
        if x == 30:
            m += 1
        for counter_index in range(k):
            # hash x
            y = a[counter_index] * x + b[counter_index]
            y = y % p
            y = y % d
            y = int(y)
            counters[counter_index, y] += 1
    f.close()
print(counters)


# query on x
x = 30
l = []
for counter_index in range(k):
    # hash x
    y = a[counter_index] * x + b[counter_index]
    y = y % p
    y = y % d
    y = int(y)
    l.append(counters[counter_index, y])
print(l)
print(int(min(l)), m)
