def integerSort(inputArray):
    arr = list(inputArray)
    
    def quicksort(items):
        if len(items) <= 1:
            return items
        pivot = items[len(items) // 2]
        left = [x for x in items if x < pivot]
        middle = [x for x in items if x == pivot]
        right = [x for x in items if x > pivot]
        return quicksort(left) + middle + quicksort(right)

    return quicksort(arr)