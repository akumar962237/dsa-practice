"""
Problem: Rearrange Array Elements by Sign
------------------------------------------
Given an array of size n with equal number of positive and negative
elements, rearrange it such that positive and negative numbers alternate,
starting with a positive number at index 0.

Assumption: The array contains an equal count of positive and negative
numbers (this is the standard constraint for this problem).

Example:
    Input:  [1, -2, -3, 4, -5, 6, 1, -9]  -> after separating by sign:
            pos = [1, 4, 6, 1], neg = [-2, -3, -5, -9]
    Output: [1, -2, 4, -3, 6, -5, 1, -9]
"""


# ------------------------- BRUTE FORCE APPROACH -------------------------
def rearrange_brute(arr):
    
    n = len(arr)
    pos = []
    neg = []

    # Step 1: separate positive and negative numbers
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    # Step 2: merge them back alternately (pos first, as required)
    result = []
    for i in range(n // 2):
        result.append(pos[i])
        result.append(neg[i])

    return result

# ---------------------------- OPTIMAL APPROACH ---------------------------
def rearrange_optimal(arr):
    
    n = len(arr)
    result = [0] * n

    pos_idx = 0   # next even index for a positive number
    neg_idx = 1   # next odd index for a negative number

    for num in arr:
        if num >= 0:
            result[pos_idx] = num
            pos_idx += 2
        else:
            result[neg_idx] = num
            neg_idx += 2

    return result


# ------------------------------- DRIVER CODE ------------------------------
if __name__ == "__main__":
    arr = [1, -2, -3, 4, -5, 6, 1, -9]

    print("Original array :", arr)
    print("Brute Force    :", rearrange_brute(arr))
    print("Optimal        :", rearrange_optimal(arr))


# Problem: Rearrange array so positive and negative numbers alternate.
# Here the count of positives and negatives may NOT be equal.
#
# Striver's approach (from A2Z DSA sheet):
# 1. Traverse the array once, put positives in one list and negatives in another.
# 2. Merge the two lists alternately (positive first, then negative).
# 3. Once the smaller list runs out, just add the remaining elements
#    of the bigger list at the end, in their original order.
#
# Note: For this variation (unequal count), there is only ONE standard
# approach in the sheet - not a separate brute force and optimal.
# It is already O(n) time and O(n) space, which is optimal for this problem.

# Example:
# Input:  [1, 2, -3, -4, -5, 6, -7, -8]
# Output: [1, -3, 2, -4, 6, -5, -7, -8]


def rearrange(arr):
    pos = []
    neg = []

    # Step 1: separate positives and negatives
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    result = []
    i = 0
    j = 0

    # Step 2: merge alternately, positive first
    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1

    # Step 3: append whatever is left over from the bigger list
    while i < len(pos):
        result.append(pos[i])
        i += 1

    while j < len(neg):
        result.append(neg[j])
        j += 1

    return result


# ------------------- DRIVER CODE -------------------
if __name__ == "__main__":
    arr = [1, 2, -3, -4, -5, 6, -7, -8]

    print("Original array :", arr)
    print("Result         :", rearrange(arr))