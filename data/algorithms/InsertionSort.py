def insertion_sort(array):
    # loop through the array
    for i in range(1, len(array)):
        # define the current element
        current = array[i]
        # define the position of the element
        position = i
        # loop through the array starting from the position of the current element
        while position > 0 and array[position - 1] > current:
            # set the current element to the position
            array[position] = array[position - 1]
            # move the position
            position -= 1
        # set the current element to the position
        array[position] = current
    return array