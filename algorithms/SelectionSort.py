def selection_sort(array):
    # loop through the array
    for i in range(len(array)):
        # define the minimum element
        min_index = i
        # loop through the array starting from the next element
        for j in range(i + 1, len(array)):
            # if the current is less than minimum
            if array[j] < array[min_index]:
                # set current as minimum
                min_index = j
        # swap
        array[i], array[min_index] = array[min_index], array[i]
    return array