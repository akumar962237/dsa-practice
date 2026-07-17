#  -----------OPTIMAL SOLUTION----------------


arr = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]


def max_consecutive_ones(arr):
    max = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    return max


print(max_consecutive_ones(arr))