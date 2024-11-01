def find_max_difference(arr):
    def max_difference_helper(arr, left, right):
        # Base case: if the array has only two elements
        if right - left == 1:
            return arr[right] - arr[left]

        # Find the middle point
        mid = (left + right) // 2

        # Recursively find the largest difference in the left and right halves
        left_diff = max_difference_helper(arr, left, mid)
        right_diff = max_difference_helper(arr, mid, right)

        # Find the minimum element in the left half
        min_left = min(arr[left : mid + 1])

        # Find the maximum element in the right half
        max_right = max(arr[mid + 1 : right + 1])

        # The largest difference that crosses the boundary
        cross_diff = max_right - min_left

        # Return the maximum of the three differences
        return max(left_diff, right_diff, cross_diff)

    return max_difference_helper(arr, 0, len(arr) - 1)


# Example usage
x = [22, 5, 8, 10, -3, 1]
print(find_max_difference(x))  # Output: 5D
