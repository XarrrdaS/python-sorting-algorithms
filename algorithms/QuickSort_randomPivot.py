import random

def quickSort_randomPivot(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[random.randint(0, len(array) - 1)]
        larger = []
        equalToPivot = []
        smaller = []
        for i in array:
            if i > pivot:
                larger.append(i)
            elif i == pivot:
                equalToPivot.append(i)
            else:
                smaller.append(i)
        return quickSort_randomPivot(smaller) + equalToPivot + quickSort_randomPivot(larger)
      