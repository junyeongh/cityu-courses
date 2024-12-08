# longest palindromic subsequence

input1 = "bbbab"
input2 = "bbabcbbcabc"


def longest_palindromic_subsequence(input: str) -> int:
    n = len(input)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if input[i] == input[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    from pprint import pprint

    pprint(dp)
    return dp[0][n - 1]


# print(longest_palindromic_subsequence(input1))
# print(longest_palindromic_subsequence(input2))

A = [-2, 3, 4, -2, -1, 6, -4, 2]


def max_subarray_sum(A: list) -> int:
    n = len(A)
    dp = [0] * n
    dp[0] = A[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + A[i], A[i])
    print(dp)
    return max(dp)


# print(max_subarray_sum(A))
