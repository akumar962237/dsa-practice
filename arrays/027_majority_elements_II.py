# ---------------------------------------------
# Problem: Majority Element II
# ---------------------------------------------
# Given an integer array nums, return all elements
# that appear more than n//3 times.
#
# There can be at most TWO majority elements.
#
# Approach:
# We use Moore's Voting Algorithm (Extended Version).
#
# Step 1:
# Find two potential majority candidates.
#
# Step 2:
# Verify whether those candidates actually occur
# more than n//3 times.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ---------------------------------------------

def majority_element(nums):
    # Candidate elements
    el1 = float('-inf')
    el2 = float('-inf')

    # Counters for candidates
    cnt1 = 0
    cnt2 = 0

    # -------------------------
    # Step 1: Find Candidates
    # -------------------------
    for num in nums:

        if cnt1 == 0 and num != el2:
            cnt1 = 1
            el1 = num

        elif cnt2 == 0 and num != el1:
            cnt2 = 1
            el2 = num

        elif num == el1:
            cnt1 += 1

        elif num == el2:
            cnt2 += 1

        else:
            cnt1 -= 1
            cnt2 -= 1

    # -------------------------
    # Step 2: Verify Candidates
    # -------------------------
    cnt1 = 0
    cnt2 = 0

    for num in nums:
        if num == el1:
            cnt1 += 1
        if num == el2:
            cnt2 += 1

    ans = []

    minimum = len(nums) // 3 + 1

    if cnt1 >= minimum:
        ans.append(el1)

    if cnt2 >= minimum:
        ans.append(el2)

    ans.sort()

    return ans


# -------------------------
# Example
# -------------------------
nums = [1, 2, 1, 3, 1, 2, 2]
print(majority_element(nums))