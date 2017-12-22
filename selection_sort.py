def find_smallest(arr, start):
    """Finds smallest number in an array."""
    smallest_element = arr[start]
    for i in range(start, len(arr)):
        if arr[i] < smallest_element:
            smallest_element = arr[i]
            start = i
    return start

def selection_sort(arr):
    """Sorts an array of ints smallest to largest. O(n^2) time."""
    for i in range(0, len(arr)):
        smallest_index = find_smallest(arr, i)
        temp = arr[i]
        arr[i], arr[smallest_index] = arr[smallest_index], temp
    return arr


test_arr = [15, 3, 34, 6, 1, 37, 11, 3, 1, 35]
print(selection_sort(test_arr))
