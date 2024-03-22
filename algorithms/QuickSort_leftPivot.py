def quickSort_leftPivot(array):
    # when none or only one element occured in the array just return it
    # to be able to move on and select a pivot
    if len(array) <= 1:
        return array
    else:
        # take the furthest left element as pivot
        pivot = array[0]
        larger = []
        smaller = []
        # loop through all elements in the array except the pivot
        for i in array[1:]:
            # if the element is larger than pivot, add it to the array in order to
            # designate a new array of larger elements than pivot 
            if i > pivot:
                larger.append(i)
            # same as above but with smaller element
            else:
                smaller.append(i)
        # recursive execution of function in order to divide arrays with smaller and larger
        # numbers compared to current pivot, as at the beggining if the array length is lower than or equal to 1 
        # it will return the exact element
        return quickSort_leftPivot(larger) + [pivot] + quickSort_leftPivot(smaller)
    