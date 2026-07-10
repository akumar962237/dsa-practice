# -----------------------------
# BRUTE FORCE APPROACH
# Time Complexity: O(N²)
# Space Complexity: O(1)
# -----------------------------

def two_sum_brute(arr, target):
    n = len(arr)

    # Check every pair
    for i in range(n):
        for j in range(i + 1, n):

            # If pair sum equals target
            if arr[i] + arr[j] == target:
                return "YES"

    return "NO"


# Example
arr = [2, 6, 5, 8, 11]
target = 14

print(two_sum_brute(arr, target))


# -----------------------------
# BETTER APPROACH (Hash Map)
# Time Complexity: O(N)
# Space Complexity: O(N)
# -----------------------------

def two_sum_hashmap(arr, target):

    visited = {}

    for i in range(len(arr)):

        current = arr[i]

        # Number needed to make target
        more_needed = target - current

        # Check if required number already exists
        if more_needed in visited:
            return "YES"

        # Store current element
        visited[current] = i

    return "NO"


# Example
arr = [2, 6, 5, 8, 11]
target = 14

print(two_sum_hashmap(arr, target))

# -----------------------------
# OPTIMAL APPROACH
# Two Pointers
# Time Complexity: O(N log N)
# Space Complexity: O(1)
# -----------------------------

def two_sum_optimal(arr, target):

    # Sort the array
    arr.sort()

    left = 0
    right = len(arr) - 1

    while left < right:

        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return "YES"

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return "NO"


# Example
arr = [2, 6, 5, 8, 11]
target = 14

print(two_sum_optimal(arr, target))