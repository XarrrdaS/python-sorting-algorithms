from algorithms.QuickSort_leftPivot import quickSort_leftPivot
from algorithms.QuickSort_randomPivot import quickSort_randomPivot

#Insertion sort, Shell sort, Selection sort, Heap sort, Quick sort (random pivot, left pivot)
if __name__ == "__main__":
    testArray_quickSortLeftPivot = [2, 6, 8, 10, 1, 2, 1, 1, 1, 2, 10]
    print('QuickSort - left pivot:')
    print(quickSort_leftPivot(testArray_quickSortLeftPivot))
    
    testArray_quickSortRandomPivot = [6, 5, 4, 6, 7, 3, 4, 6, 7, 4, 111, 12, 0]
    print('\nQuickSort - random pivot:')
    print(quickSort_randomPivot(testArray_quickSortRandomPivot))
