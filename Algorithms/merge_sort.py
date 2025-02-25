import sys

def merge_sort(numbers, low, high):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort(numbers, low, mid)
        merge_sort(numbers, mid + 1, high)
        merge(numbers, low, mid, high)

def merge(numbers, low, mid, high):
    left_half = numbers[low:mid + 1]
    right_half = numbers[mid + 1:high + 1]
    i = 0
    j = 0
    k = low
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            numbers[k] = left_half[i]
            i += 1
        else:
            numbers[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        numbers[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        numbers[k] = right_half[j]
        j += 1
        k += 1

numbers = list(map(int, sys.argv[1:]))
merge_sort(numbers, 0, len(numbers) - 1)
print("Sorted numbers:", numbers)