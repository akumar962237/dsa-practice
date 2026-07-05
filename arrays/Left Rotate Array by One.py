arr = [1, 2, 3, 4, 5]
k = 2

def rotate(arr, k):
    n = len(arr)
    k = k % n  # Handle k > n
    
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    return arr

result = rotate(arr, k)
print("Array after rotation:", result)