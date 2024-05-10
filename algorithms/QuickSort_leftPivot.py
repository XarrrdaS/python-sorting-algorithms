def quickSort_leftPivot(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        larger = []
        smaller = []
        for i in array[1:]:
            if i > pivot:
                larger.append(i)
            else:
                smaller.append(i)
        return quickSort_leftPivot(smaller) + [pivot] + quickSort_leftPivot(larger)
    