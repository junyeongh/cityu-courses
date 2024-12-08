import pandas as pd
import pickle

data = pd.read_excel("Online Retail.xlsx")  # read excel by pandas
print(data)

data = data.values
data = data[:, 0:2]  # we only need the first two columns
print(data)

order_list = list()  # empty list, list of our final data

order_set = set()  # empty orderSet
InvoiceNo = data[0, 0]  # the current InvoiceNo
# go though our data
for i in range(len(data)):
    if data[i, 0] == InvoiceNo:
        # add a new item in orderSet
        order_set.add(str(data[i, 1]))
    else:
        # this orderSet is end
        order_list.append(order_set)
        InvoiceNo = data[i, 0]  # next InvoiceNo
        order_set = set()
        order_set.add(data[i, 1])

print(order_list[0:10])

# To store our result by pickle
# f = open("order_list.pickle", 'wb')
# pickle.dump(order_list, f)
with open("order_list.pickle", "wb") as f:
    pickle.dump(order_list, f)
