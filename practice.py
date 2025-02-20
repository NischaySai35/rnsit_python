def merge_sort(numbers, low, high):
    if low < high:
        mid = low + (high - low) // 2  
        
        merge_sort(numbers, low, mid)    
        merge_sort(numbers, mid + 1, high) 
        merge(numbers, low, mid, high)   

def merge(numbers, low, mid, high):

    array1 = numbers[low:mid + 1]
    array2 = numbers[mid + 1:high + 1]

    i, j, k = 0, 0, low
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            numbers[k] = array1[i]
            i += 1
        else:
            numbers[k] = array2[j]
            j += 1
        k += 1

    while i < len(array1):
        numbers[k] = array1[i]
        i += 1
        k += 1

    while j < len(array2):
        numbers[k] = array2[j]
        j += 1
        k += 1

arr = list(map(int,input('Enter nos . ').split()))
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
