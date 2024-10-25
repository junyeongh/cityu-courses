def find_smallest_intervals(elements, interval_length):
    # Step 1: Sort the list of elements
    elements.sort()

    # Step 2: Initialize variables
    intervals = []
    i = 0
    n = len(elements)

    # Step 3: Iterate through the list
    while i < n:
        # Start a new interval from the current element
        start = elements[i]
        end = start + interval_length

        # Add the interval to the list
        intervals.append((start, end))

        # Move the index to the first element not covered by the current interval
        while i < n and elements[i] <= end:
            i += 1

    return intervals

# Example usage:
elements = [1.5, 2.0, 2.1, 5.7, 8.8, 9.1, 10.2]
interval_length = 2
print(find_smallest_intervals(elements, interval_length))
