def max_weight_independent_set(weights, distances, L):
    n = len(weights)

    # dp[i][j] represents max weight considering nodes 1..i
    # where j is index of last included node (0 if none)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # For tracking the solution
    prev = [[0] * (n + 1) for _ in range(n + 1)]

    # Base case: considering only first node
    dp[1][0] = 0  # don't include it
    dp[1][1] = weights[0]  # include it

    # For each node i
    for i in range(2, n + 1):
        # For each possible last included node j
        for j in range(i):
            # Don't include node i
            dp[i][j] = dp[i - 1][j]
            prev[i][j] = j

            # Try to include node i if possible
            can_include = True

            # If we had included a node before (j > 0)
            if j > 0:
                # Calculate distance from j to i
                dist = sum(distances[k] for k in range(j - 1, i - 1))
                if dist < L:
                    can_include = False

            if can_include:
                # Check if including i gives better result
                new_weight = dp[i - 1][j] + weights[i - 1]
                if new_weight > dp[i][i]:
                    dp[i][i] = new_weight
                    prev[i][i] = j

    # Find maximum in last row
    max_weight = 0
    last_included = 0
    for j in range(n + 1):
        if dp[n][j] > max_weight:
            max_weight = dp[n][j]
            last_included = j

    # Reconstruct solution
    solution = []
    i = n
    while i > 0:
        if i == last_included:
            solution.append(i)
            last_included = prev[i][last_included]
        i -= 1

    from pprint import pprint
    pprint(dp)
    return max_weight, solution[::-1]


if __name__ == "__main__":
    # Input values from visualization
    weights = [5, 2, 4, 1, 3]  # weights of nodes v₁ to v₅
    distances = [2, 3, 2, 2]  # distances between consecutive nodes
    L = 4  # minimum distance requirement

    # Call the function
    max_weight, solution = max_weight_independent_set(weights, distances, L)

    print(f"Maximum weight: {max_weight}")
    print(f"Selected nodes: {solution}")
