#Sorting

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
   

    #i is keeping track of how many times you've gone through the list
    #which means i is how many numbers have been sorted
    #so i represents how many numbers at the end of the list are in the correct spot
    #which means, that is "i" many numbers we don't have to look at
    for i in range(len(lst) - 1): #sets the ending point for the 2nd sort's starting point
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def merge_lists(list1, list2):
    """Given two sorted lists of integers, return a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    result_list = []
    while len(list1) > 0 or len(list2) > 0:
        # if items left in both lists
        # compare first items of each list
        if list1 == []:
            result_list.append(list2.pop(0))
        elif list2 == []:
            result_list.append(list1.pop(0))
        elif list1[0] < list2[0]:
            # append and rm first item of lst1
            result_list.append(list1.pop(0))
        else:
            # append and rm first item of lst2
            result_list.append(list2.pop(0))

    print "returning", result_list
    return result_list
 


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, return a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    if len(lst) < 2:  # if length of lst is 1, return lst
        return lst

    mid = int(len(lst) / 2)  # index at half the list
    lst1 = merge_sort(lst[:mid])  # divide list in half
    lst2 = merge_sort(lst[mid:])  # assign other half

    # Compare first items of each pair of lists & interleave

    result_list = []
    print lst1, lst2
    return_list = merge_lists(lst1, lst2)
    return return_list




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print