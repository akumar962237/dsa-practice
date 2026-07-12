# ============================================
# Problem: Maximum Sum Subarray (Kadane's Algorithm)
# Find the maximum sum of a contiguous subarray in an array.
# Array can contain negative numbers too.
# ============================================


# ---------- BRUTE FORCE APPROACH ----------
# Try every possible subarray, calculate its sum,
# and keep track of the maximum sum found.
# Time Complexity: O(n^2)
# Space Complexity: O(1)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def max_subarray_sum_brute(arr):
    n = len(arr)
    max_sum = arr[0]  # start with first element as reference

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


print("Brute Force Result:", max_subarray_sum_brute(arr))



# ---------- OPTIMAL SOLUTION (Kadane's Algorithm) ----------
# We solve this using Kadane's Algorithm.
# The key idea: at each element, decide whether to
# extend the previous subarray or start a new one.
#
# current_sum -> best sum ending at current index
# max_sum     -> best sum found so far overall
#
# If current_sum becomes negative, it can only hurt future
# sums, so we reset it to 0 (start fresh from next element).
#
# Time Complexity: O(n)
# Space Complexity: O(1)


def max_subarray_sum_optimal(arr):
    max_sum = arr[0]
    current_sum = 0
    
    start = 0          # tracks where current subarray starts
    temp_start = 0      # temporary start pointer
    end = 0             # tracks where max subarray ends

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start   # lock in the current subarray's start
            end = i              # lock in current index as end

        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1   # next element becomes potential new start

    subarray = arr[start:end + 1]
    return max_sum, subarray


arr = [-2, 1, -3, 4, -1, 2, 1, 5, 4]
max_sum, subarray = max_subarray_sum_optimal(arr)
print("Maximum Sum:", max_sum)
print("Subarray:", subarray)
