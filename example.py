import sys
from algorithms.InsertionSort import insertion_sort
from algorithms.HeapSort import heapSort
from algorithms.QuickSort_leftPivot import quickSort_leftPivot
from algorithms.QuickSort_randomPivot import quickSort_randomPivot
from algorithms.SelectionSort import selection_sort
from algorithms.ShellSort import shell_sort


def sort_using_algorithm(data, algorithm):
    # This function takes the algorithm identifier as input
    # However, it always uses the sorted function in Python

    sorted_data = sorted(data)

    return sorted_data


def chooseAlgorithm(data, algorithmNum):
    if algorithmNum == 1:
        insertion_sort(data)
    if algorithmNum == 2:
        shell_sort(data)
    if algorithmNum == 3:
        selection_sort(data)
    if algorithmNum == 4:
        heapSort(data)
    if algorithmNum == 5:
        quickSort_leftPivot(data)
    if algorithmNum == 6:
        quickSort_randomPivot(data)


def main():
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    # Read input data from standard input until the end of file (EOF)
    input=sys.stdin.read().split()
    try:
        data = [int(x) for x in input[1:]]
    except EOFError:
        print("Error reading input.")

    # Perform sorting using the specified algorithm (ignored in this example)
    sorted_data = chooseAlgorithm(data, algorithm_number)

    # Print the sorted data
    print("Sorted data:", sorted_data)

if __name__ == "__main__":
    main()