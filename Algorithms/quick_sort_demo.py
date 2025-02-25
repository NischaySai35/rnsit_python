import quick_sort

print('Enter the input numbers')
numbers = list(map(int, input().split()))

print(f'Input Array is: {numbers}')
quick_sort.quick_sort(numbers, 0, len(numbers)-1)
print(f'Sorted Array is: {numbers}')