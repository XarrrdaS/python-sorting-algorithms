def shell_sort(array):
    # define the interval
    sedgewick = [0] * round(len(array)/2)
    for s in range(round(len(array)/2)):
        sedgewick[s] = 4**(s+1) + 3*2**s + 1
    interval = sedgewick[:-1]
    # print(interval)
    # interval = len(array) // 2
    # loop through the array
    temp = round(len(array)/2)-1
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
        temp = temp-1
        interval = sedgewick[temp]
        print(interval)
    return array

print(shell_sort([5, 3, 8]))