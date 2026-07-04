arr = [1,5,2,3,7,4,8]

def largest_element(arr):
    max_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num
result = largest_element(arr)
print("The largest element in the array is:", result)