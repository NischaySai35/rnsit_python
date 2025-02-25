import sys

def insertion_sort(arr):
    for i in range(1, len(inp_list)):
        ele = arr[i]
        j = i-1
        while j >= 0 and ele < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = ele
    return arr

inp_list = sys.argv[1:]
print("Before sorting - ", end=" ")
for i in inp_list:
    print(i, end=" ")
print("\nAfter sorting  - ", end=" ")
sorted_list = insertion_sort(inp_list)
for i in sorted_list:
    print(i, end=" ")