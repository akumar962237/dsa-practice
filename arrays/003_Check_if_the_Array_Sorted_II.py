
arr = [1, 2, 3, 4, 5]

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
result  = is_sorted(arr)
print("The array is sorted:", result)    