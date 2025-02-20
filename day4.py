import sys

def insertion_sort_strings(arr):
    for i in range(1, len(arr)):  # Start from the second element
        key = arr[i]
        j = i - 1

        # Move elements that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Insert the key in the correct position

arr = sys.argv[1:]  # Get words from CLI arguments

print("User words :",arr)
# Sort the strings
insertion_sort_strings(arr)

# Print sorted strings
print("Sorted words:", " ".join(arr))
