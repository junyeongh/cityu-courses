# Knapsack problem
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
# print(f"{n=}, {k=}")

items = [list(map(int, input().split())) for _ in range(n)]  # weight, value
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= items[i - 1][0]:
            dp[i][j] = max(
                items[i - 1][1] + dp[i - 1][j - items[i - 1][0]], dp[i - 1][j]
            )
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])
