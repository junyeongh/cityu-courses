def zero_one_knapsack(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(capacity + 1):
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    # Backtrack to find the selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][1]

    from pprint import pprint
    pprint(dp)
    print("Selected items:", selected_items)
    return dp[n][capacity]

if __name__ == "__main__":
    # item = (value, weight)
    items = [
        (1, 1), # item 1
        (3, 2), # item 2
        (2, 1), # item 3
        (4, 3), # item 4
        (2, 3), # item 5
        (6, 2), # item 6
    ]

    capacity = 5

    result = zero_one_knapsack(items, capacity)
    print("Maximum value:", result)
