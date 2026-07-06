arr = [1,2,3,4,5]

def left_rotate(arr, k):
    n = len(arr)
    k = k % n
    
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)
    return arr

# Test with different K values
print(left_rotate([1,2,3,4,5], 1))  # [2,3,4,5,1] ✓
print(left_rotate([1,2,3,4,5], 2))  # [3,4,5,1,2] ✓
print(left_rotate([1,2,3,4,5], 3))  # [4,5,1,2,3] ✓
print(left_rotate([1,2,3,4,5], 4))  # [5,1,2,3,4] ✓