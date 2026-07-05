arr = [1,3,2,4,6,5,8,7]
def second_largest(arr):
    first = arr[0]
    second = -1
    for i in range(1, len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] < first:
            second = arr[i]
    return second
result = second_largest(arr)
print("The second largest element in the array is:", result)