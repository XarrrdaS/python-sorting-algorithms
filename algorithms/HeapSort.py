def createHeap(array, numberElements, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < numberElements and array[i] < array[left]:
        largest = left
    if right < numberElements and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        createHeap(array, numberElements, largest)
        
def heapSort(array):
    numberElements = len(array)
    for i in range(numberElements // 2 - 1, -1, -1):
        createHeap(array, numberElements, i)
    for i in range(numberElements - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        createHeap(array, i, 0)
    return array