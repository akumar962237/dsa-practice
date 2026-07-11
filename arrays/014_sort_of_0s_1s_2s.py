#---------BRUTE FORCE APPROACH----------------
def sort_of_0s_1s_2s(arr):
    n = len(arr)
    # Create a new array to hold the sorted values
    sorted_arr = [0] * n
    index = 0

    # First pass: place all 0s in the new array
    for i in range(n):
        if arr[i] == 0:
            sorted_arr[index] = 0
            index += 1

    # Second pass: place all 1s in the new array
    for i in range(n):
        if arr[i] == 1:
            sorted_arr[index] = 1
            index += 1

    # Third pass: place all 2s in the new array
    for i in range(n):
        if arr[i] == 2:
            sorted_arr[index] = 2
            index += 1

    return sorted_arr

arr = [0,1,2,0,0,1,1,2,2,0,2,1,0,1,2]
print(sort_of_0s_1s_2s(arr))


#------------OPTIMAL SOLUTION----------------
# We solve this using the Dutch National Flag Algorithm.
# It uses 3 pointers (low, mid, high) to sort the array
# of 0s, 1s, and 2s in a single pass, without extra space.
#
# low  -> boundary for 0s (everything before low is 0)
# mid  -> current element being checked
# high -> boundary for 2s (everything after high is 2)

def sort_of_0s_1s_2s(arr):
    n = len(arr)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

arr = [0,1,2,0,0,1,1,2,2,0,2,1,0,1,2]
print(sort_of_0s_1s_2s(arr))