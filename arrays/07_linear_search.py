arr = [1, 2, 3, 5, 4, 7, 6]

def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

print(linear_search(arr, 5))