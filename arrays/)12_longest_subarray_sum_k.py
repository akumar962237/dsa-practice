#-------BRUTE FORCE APPROACH--------
def longest_subarray_sum_k(arr, k):
    max_length = 0
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == k:
                max_length = max(max_length, j - i + 1)
    return max_length   
print(longest_subarray_sum_k([1, 2, 3, 4, 5], 9))  # Output: 2 (subarray [4, 5])