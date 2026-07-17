"""
=========================================================
            LEADERS IN AN ARRAY (Python)
=========================================================

Problem Statement:
------------------
Given an array of integers, find all the leaders in the array.

A leader is an element that is greater than all the elements
to its right. The rightmost element is always considered a leader.

Example:
---------
Input:
    [10, 22, 12, 3, 0, 6]

Output:
    [22, 12, 6]

Approaches:
-----------
1. Brute Force Approach
   - Compare every element with all elements to its right.
   - Time Complexity : O(n²)
   - Space Complexity: O(n)

2. Optimal Approach
   - Traverse the array from right to left while maintaining
     the maximum element seen so far.
   - Time Complexity : O(n)
   - Space Complexity: O(n)
=========================================================
"""

# =====================================================
# BRUTE FORCE APPROACH
# =====================================================

arr = [10, 22, 12, 3, 0, 6]

def find_leaders_brute(arr):
    """
    Finds all leaders using the Brute Force approach.

    Logic:
    ------
    For every element, check all the elements on its right.
    If no greater element exists, then it is a leader.
    """

    n = len(arr)
    ans = []

    # Traverse every element
    for i in range(n):

        # Assume current element is a leader
        leader = True

        # Check all elements on the right
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                leader = False
                break

        # Store the leader
        if leader:
            ans.append(arr[i])

    return ans


print("Brute Force Output :", find_leaders_brute(arr))


# =====================================================
# OPTIMAL APPROACH
# =====================================================

def find_leaders_optimal(arr):
    """
    Finds all leaders using the Optimal approach.

    Logic:
    ------
    Traverse from right to left while keeping track of
    the maximum element encountered so far.

    If the current element is greater than the maximum,
    it is a leader.
    """

    ans = []
    maxi = float('-inf')      # Smallest possible value

    # Traverse from right to left
    for i in range(len(arr) - 1, -1, -1):

        # Current element is a leader
        if arr[i] > maxi:
            ans.append(arr[i])

        # Update maximum element
        maxi = max(maxi, arr[i])

    # Reverse to restore original order
    ans.reverse()

    return ans


print("Optimal Output     :", find_leaders_optimal(arr))