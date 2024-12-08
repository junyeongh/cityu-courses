import math
import itertools
import heapq

freq = {}
with open("patterns_Apriori.txt") as f:
    for line in f:
        line = line[:-1].split(":")
        pattern = line[0].split(",")
        pattern = [int(i) for i in pattern]
        freq[tuple(pattern)] = int(line[1])

k = 500
C_list = [500000, 750000, 1000000]
m = math.ceil(math.log2(k + 1))
L_list = []
minSup_A = []
for C in C_list:
    counter = {}
    L = 0
    A = []
    with open("trans.txt") as f:
        for line in f:
            line = line[:-1].split("\t")
            line = [int(i) for i in line]
            l_m = m if len(line) > m else len(line)
            for r in range(1, l_m + 1):
                for pattern in itertools.combinations(line, r):
                    L += 1
                    pattern = tuple(sorted(pattern))
                    if pattern in counter:
                        counter[pattern] += 1
                    elif len(counter) < C:
                        counter[pattern] = 1
                    else:
                        for key, value in list(counter.items()):
                            if (value - 1) == 0:
                                del counter[key]
                            else:
                                counter[key] -= 1
    dict_sorted = heapq.nlargest(k, counter, key=counter.get)
    k_largest = counter[dict_sorted[-1]]
    for key, value in list(counter.items()):
        if value > (k_largest - L / (C + 1)):
            A.append(freq[key])

    minSup_A.append(min(A))
    L_list.append(L)

print("L is: ", L_list[0])
for i in range(3):
    print("when C is: ", C_list[i], " minSup(A) is : ", minSup_A[i])
# L is:  59340244
# when C is:  500000  minSup(A) is :  1037
# when C is:  750000  minSup(A) is :  1077
# when C is:  1000000  minSup(A) is :  1098
