import sys

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid+1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return 0

arr = list(map(int, sys.argv[1:-1]))
key = int(sys.argv[-1])

pos = binary_search(arr, key)
if pos:
    print("Element found at position", pos)
else:
    print("Element not found")