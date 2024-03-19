def createHeap(array, numberElements, i):
    # take largest element (root)
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
        # recursion in order to create new subheap with largest root
        createHeap(array, numberElements, largest)
        
def heapSort(array):
    numberElements = len(array)
    # build a max heap (every child element must be smaller than the parent element)
    # loop from the middle element to the first element
    # after that the largest element is on the top of the array
    for i in range(numberElements // 2 - 1, -1, -1):
        createHeap(array, numberElements, i)
    # extract elements from the heap one by one in descending order
    for i in range(numberElements - 1, 0, -1):
        # move the largest element (first in array) with current element
        # after that the largest element is in the right place in the array 
        array[i], array[0] = array[0], array[i]
        # call the createHeap function on the reduced heap to return the heap 
        # property, after that the largest element of the reduced heap 
        # is at the beggining of this part of the array
        createHeap(array, i, 0)
    return array
