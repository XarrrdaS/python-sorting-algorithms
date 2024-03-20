def shell_sort(array):
    # define the gap
    gap = len(array) // 2
    # loop through the array
    while gap > 0:
        # loop through the array starting from the gap
        for i in range(gap, len(array)):
            # define the current element
            current = array[i]
            # define the position of the element
            position = i
            # loop through the array starting from the position of the current element
            while position >= gap and array[position - gap] > current:
                # swap the elements
                array[position] = array[position - gap]
                # move the position
                position -= gap
            # set the current element to the position
            array[position] = current
        # divide the gap by 2
        gap //= 2
    return array