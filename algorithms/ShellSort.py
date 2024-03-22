def shell_sort(array):
    # define the interval
    interval = len(array) // 2
    # loop through the array
    while interval > 0:
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
        # divide the interval by 2
        interval //= 2
    return array