import random

def quickSort_randomPivot(array):
    # when none or only one element occured in the array just return it
    # to be able to move on and select a pivot
    if len(array) <= 1:
        return array
    else:
        # take the random element as pivot
        pivot = array[random.randint(0, len(array) - 1)]
        larger = []
        equalToPivot = []
        smaller = []
        # loop through all elements in the array
        for i in array:
            # if the element is larger than pivot, add it to the array in order to
            # designate a new array of larger elements than pivot 
            if i > pivot:
                larger.append(i)
            # same as above but with equal to pivot element
            elif i == pivot:
                equalToPivot.append(i)
            # same as above but with smaller than pivot element
            else:
                smaller.append(i)
        # recursive execution of function in order to divide arrays with smaller and larger
        # numbers compared to current pivot, as at the beggining if the array length is lower than or equal to 1 
        # it will return the exact element
        return quickSort_randomPivot(smaller) + equalToPivot + quickSort_randomPivot(larger)
    