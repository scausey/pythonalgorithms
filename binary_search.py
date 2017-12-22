def binary_search(ls, item):
    """An O(log n) search algrithm."""
    ls.sort()
    low = 0
    high = len(ls) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = ls[mid]
        if guess == item:
            print("Item found!")
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    print("Item doesn't exist!")
    return None


my_list = [13, 7, 11, 4, 1]
binary_search(my_list, 13)
