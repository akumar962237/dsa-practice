"""
Problem:
--------
Given an integer array and an integer K, find the length of the
longest subarray whose sum is equal to K.

Approach:
---------
Brute Force

- Generate every possible subarray.
- Calculate the sum of each subarray.
- If the sum equals K, update the maximum length.

Time Complexity:
----------------
O(n²)

Space Complexity:
-----------------
O(1)
"""

def longest_subarray_sum_k_brute(arr, k):
    n = len(arr)
    max_length = 0

    # Generate all possible starting indices
    for i in range(n):

        current_sum = 0

        # Extend the subarray one element at a time
        for j in range(i, n):

            current_sum += arr[j]

            # Check whether the current subarray sum equals K
            if current_sum == k:
                max_length = max(max_length, j - i + 1)

    return max_length


# Driver Code
arr = [1, 2, 3, 4, 5]
k = 9

print("Longest Subarray Length:", longest_subarray_sum_k_brute(arr, k))


"""
Problem:
--------
Given an integer array and an integer K, find the length of
the longest subarray whose sum equals K.

Approach:
---------
Prefix Sum + HashMap

- Maintain a running prefix sum.
- Store the first occurrence of every prefix sum.
- If (current_sum - K) exists in the hashmap,
  then a subarray with sum K exists.

This approach works for:
- Positive Numbers
- Negative Numbers
- Zero

Time Complexity:
----------------
O(n)

Space Complexity:
-----------------
O(n)
"""

def longest_subarray_sum_k_prefix(arr, k):

    # Stores prefix_sum : first_index
    prefix_map = {}

    current_sum = 0
    max_length = 0

    for i in range(len(arr)):

        # Calculate prefix sum
        current_sum += arr[i]

        # If prefix sum itself equals K
        if current_sum == k:
            max_length = i + 1

        # Check if a previous prefix sum exists
        if (current_sum - k) in prefix_map:
            max_length = max(
                max_length,
                i - prefix_map[current_sum - k]
            )

        # Store only the first occurrence
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return max_length


# Driver Code
arr = [1, 2, 3, 4, 5]
k = 9

print("Longest Subarray Length:", longest_subarray_sum_k_prefix(arr, k))

"""
Problem:
--------
Given an integer array containing only positive integers
and an integer K, find the length of the longest subarray
whose sum equals K.

Approach:
---------
Sliding Window

- Maintain two pointers (left and right).
- Expand the window by moving the right pointer.
- Shrink the window whenever the sum exceeds K.
- If the sum becomes K, update the maximum length.

Note:
-----
This approach works ONLY for positive numbers.

Time Complexity:
----------------
O(n)

Space Complexity:
-----------------
O(1)
"""

def longest_subarray_sum_k_sliding(arr, k):

    left = 0
    right = 0

    current_sum = arr[0]
    max_length = 0
    n = len(arr)

    while right < n:

        # Shrink the window until sum <= K
        while left <= right and current_sum > k:
            current_sum -= arr[left]
            left += 1

        # If sum equals K, update answer
        if current_sum == k:
            max_length = max(max_length, right - left + 1)

        # Expand the window
        right += 1

        if right < n:
            current_sum += arr[right]

    return max_length


# Driver Code
arr = [1, 2, 3, 4, 5]
k = 9

print("Longest Subarray Length:", longest_subarray_sum_k_sliding(arr, k))