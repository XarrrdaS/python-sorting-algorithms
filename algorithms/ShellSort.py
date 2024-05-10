def shell_sort(array):
    intervals = []
    k = 0
    intervals.append(1)
    while True:
        interval = 4**(k + 1) + 3 * 2**k + 1
        if interval >= len(array):
            break
        intervals.append(interval)
        k += 1

    for interval in reversed(intervals):
        for i in range(interval, len(array)):
            current = array[i]
            position = i
            while position >= interval and array[position - interval] > current:
                array[position] = array[position - interval]
                position -= interval
            array[position] = current
    return array