def createHeap(array, numberElements, i):
    # take largest element
    largest = i
    # element to the left of the largest
    left = 2 * i + 1
    # element to the right of the largest
    right = 2 * i + 2
    # check if the element on the left is greater than the largest
    if left < numberElements and array[i] < array[left]:
        largest = left
    # check if the element on the right is greater than the largest
    if right < numberElements and array[largest] < array[right]:
        largest = right
    # swap the largest element if current isn't the largest one
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        # recursion in order to create the whole heap
        createHeap(array, numberElements, largest)
        
def heapSort(array):
    numberElements = len(array)
    # We build a max heap
    for i in range(numberElements//2 - 1, -1, -1):
        createHeap(array, numberElements, i)
    # We extract elements from the heap one by one
    for i in range(numberElements-1, 0, -1):
        # We move the current largest to the end
        array[i], array[0] = array[0], array[i]
        # We call the createHeap function on the reduced heap
        createHeap(array, i, 0)
    return array

arr = [12, 11, 13, 5, 6, 7, 32, 5, 4, 3, 2, 0]
print(heapSort(arr))
