def binary_search(ls, item):
    """A log n search algrithm. Cuts items to search through in half each time
    through."""
    ls.sort()
    print("Sorted list: " + str(ls))
    print("Item: " + str(item))
    low = 0
    high = len(ls) - 1

    while low <= high:
        print("Low: " + str(ls[low]))
        print("High: " + str(ls[high]))
        mid = int((low + high) / 2)
        guess = ls[mid]
        print("Guess: " + str(guess))
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
