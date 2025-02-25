import sys

arr = sys.argv[1:]

def optimized_bubble_sort():
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


print("Before sorting - ", end=" ")
for i in arr:
    print(i, end=" ")
print("\nAfter sorting  - ", end=" ")
optimized_bubble_sort()
for i in arr:
    print(i, end=" ")