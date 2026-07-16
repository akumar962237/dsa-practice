arr = [2, 1, 5, 3, 4, 0, 0]


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def reverse(arr, start, end):
    while start < end:
        swap(arr, start, end)
        start += 1
        end -= 1


def next_permutation():
    ind = -1
    n = len(arr)

    # Find the breakpoint
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            ind = i
            break

    # If no breakpoint exists
    if ind == -1:
        reverse(arr, 0, n - 1)
        return arr

    # Find the first element greater than arr[ind]
    for i in range(n - 1, ind, -1):
        if arr[i] > arr[ind]:
            swap(arr, i, ind)
            break

    # Reverse the remaining part
    reverse(arr, ind + 1, n - 1)

    return arr


print(next_permutation())
