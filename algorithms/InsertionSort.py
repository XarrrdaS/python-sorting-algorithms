def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        position = i
        while position > 0 and array[position - 1] > current:
            array[position] = array[position - 1]
            position -= 1
        array[position] = current
    return array