from algorithms.QuickSort_leftPivot import quickSort_leftPivot
from algorithms.QuickSort_randomPivot import quickSort_randomPivot
from algorithms.HeapSort import heapSort
from algorithms.ShellSort import shell_sort
from algorithms.SelectionSort import selection_sort
from algorithms.InsertionSort import insertion_sort

#Insertion sort, Shell sort, Selection sort, Heap sort, Quick sort (random pivot, left pivot)
if __name__ == "__main__":
    testArray_quickSortLeftPivot = [2, 6, 8, 10, 1, 2, 1, 1, 1, 2, 10]
    print('QuickSort - left pivot:')
    print(quickSort_leftPivot(testArray_quickSortLeftPivot))
    
    testArray_quickSortRandomPivot = [6, 5, 4, 6, 7, 3, 4, 6, 7, 4, 111, 12, 0]
    print('\nQuickSort - random pivot:')
    print(quickSort_randomPivot(testArray_quickSortRandomPivot))
    
    testArray_heapSort = [12, 11, 13, 5, 6, 7, 32, 5, 4, 3, 2, 0, 123, 123, 132, 0, 0]
    print('\nHeapSort:')
    print(heapSort(testArray_heapSort))

    testArray_shellsort = [12, 11, 13, 5, 6, 7, 32, 5, 4, 3, 2, 0, 432, 2134]
    print('\nShellSort:')
    print(shell_sort(testArray_shellsort))

    testArray_selectionsort = [12, 11, 13, 5, 6, 7, 32, 5, 4, 3, 2, 0, 124, 123]
    print('\nSelection_Sort:')
    print(selection_sort(testArray_selectionsort))

    testArray_insertionsort = [12, 11, 13, 5, 6, 7, 32, 5, 4, 3, 2, 0, 9122, 0, 0]
    print('\nInsertion_Sort:')
    print(insertion_sort(testArray_insertionsort))