import pickle


# -----------------------------------------------------------
def update_candidates_dict(frequent_list):
    old_candidates_list = list()
    for candidate in frequent_list:
        candidate = list(candidate)
        candidate.sort()
        old_candidates_list.append(candidate)

    # the size of old candidate
    size = len(old_candidates_list[0])

    new_candidates_list = list()
    # i = 0, j = 1, 2, 3, ..., m-1
    # i = 1, j = 2, ..., m-1
    # i = 2, j = 3, ..., m-1
    # ...
    # i = m-2, j = m-1
    for i in range(len(old_candidates_list) - 1):
        for j in range(i+1, len(old_candidates_list)):
            candidateA = list(old_candidates_list[i])
            candidateB = list(old_candidates_list[j])
            agree = True    # they have a possible father candidate
            for k in range(size-1):
                if candidateA[k] != candidateB[k]:
                    agree = False
                    break
            if agree:
                candidateC = candidateA.copy()
                candidateC.extend(candidateB)
                new_candidates_list.append(candidateC)

    candidates_dict = dict()
    for candidate in new_candidates_list:
        candidates_dict[tuple(candidate)] = 0    # add a candidate in candidates_dict with count 0
    return candidates_dict


# -----------------------Start Here------------------------------------
# load data set
f = open("order_list.pickle", 'rb')
order_list = pickle.load(f)
# order_list = order_list[0:1000]
print(order_list[0:10])

# set some parameters
min_sup = 500

final_output_list = list()    # list of final output

# --------------------------------------------------------
# the initial candidates_dict are all single item
candidates_dict = dict()
for order in order_list:
    for item in order:
        item = tuple([item])
        if item not in candidates_dict:
            candidates_dict[item] = 0    # add an item in candidates_dict with count 0

print("initial candidates_dict")
print(candidates_dict)
print("length of initial candidates_dict")
print(len(candidates_dict))

# --------------------------------------------------------
# core code -> Apriori Algorithm
print()
while True:
    print()
    print("Start Scan the data set...")
    # go though the order_list
    for order in order_list:
        for candidate in candidates_dict:
            temp_set = set()
            for item in candidate:
                temp_set.add(item)
            if temp_set.issubset(order):      # check issubset
                candidates_dict[candidate] += 1  # count

    # check frequency
    frequent_list = list()
    for candidate in candidates_dict:
        if candidates_dict[candidate] >= min_sup:
            frequent_list.append(candidate)
    print("frequent_list:")
    print(frequent_list)
    print("length of frequent_list:")
    print(len(frequent_list))
    if len(frequent_list) == 0:
        break

    final_output_list.extend(frequent_list)

    # update candidates_dict
    candidates_dict = update_candidates_dict(frequent_list)
    print("length of new candidates_dict")
    print(len(candidates_dict))
