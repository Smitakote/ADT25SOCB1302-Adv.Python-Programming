import numpy as np

# Create a one-dimensional array from 1 to 10
arr = np.arange(1, 11)
print("Original Array:", arr)

# Perform slicing operations
print("First five elements:", arr[:5])
print("Last five elements:", arr[5:])
print("Elements from index 2 to 6:", arr[2:7])
print("Every second element:", arr[::2])

# Calculate statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Apply broadcasting
arr = arr + 5
print("After adding 5:", arr)

arr = arr * 2
print("After multiplying by 2:", arr)
