import random
import os

# Ensure the directory exists
os.makedirs("data_stream", exist_ok=True)

# we will generate 100 txt files
# In each file, there are 10000 integers and each integer in [1, 1000]
for i in range(100):
    f = open("data_stream/stream" + str(i) + ".txt", "w")
    for j in range(10000):
        x = random.randint(1, 1000)
        f.write(str(x))
        f.write("\n")
    f.close()
