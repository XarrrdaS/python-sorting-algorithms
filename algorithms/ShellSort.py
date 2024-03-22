def shell_sort(array):
    # define the intervals using Sedgewick's sequence
    intervals = []
    k = 0
    intervals.append(1)
    while True:
        interval = 4**(k + 1) + 3 * 2**k + 1
        if interval >= len(array):
            break
        intervals.append(interval)
        k += 1

    # loop through the intervals in reverse order
    for interval in reversed(intervals):
        # loop through the array starting from the interval
        for i in range(interval, len(array)):
            # define the current element
            current = array[i]
            # define the position of the element
            position = i
            # loop through the array starting from the position of the current element
            while position >= interval and array[position - interval] > current:
                # swap the elements
                array[position] = array[position - interval]
                # move the position
                position -= interval
            # set the current element to the position
            array[position] = current
    return array

print(shell_sort([5, 3, 8, 5, 6, 7, 8]))