# ============================================
# Problem: Set Matrix Zeroes
# If an element in the matrix is 0, set its entire
# row and column to 0. Do this for all such elements.
# ============================================

matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]


# ---------- BRUTE FORCE APPROACH ----------
# For every 0 found, mark its row and column using
# a placeholder value (-1) instead of 0 directly
# (so we don't confuse original 0s with newly set 0s
# while still scanning the matrix).
# Time Complexity: O((n*m) * (n+m))
# Space Complexity: O(1) extra (but modifies in-place with markers)

def set_zeroes_brute(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # mark entire row with -1 (temporary marker)
                for k in range(m):
                    if matrix[i][k] != 0:
                        matrix[i][k] = -1
                # mark entire column with -1
                for k in range(n):
                    if matrix[k][j] != 0:
                        matrix[k][j] = -1

    # convert all -1 markers to actual 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

    return matrix


import copy
print("Brute Force:", set_zeroes_brute(copy.deepcopy(matrix)))


# ---------- BETTER APPROACH ----------
# Use two extra arrays (row[] and col[]) to mark
# which rows and columns need to be zeroed,
# instead of modifying matrix while scanning it.
# Time Complexity: O(n*m)
# Space Complexity: O(n + m)

def set_zeroes_better(matrix):
    n = len(matrix)
    m = len(matrix[0])

    row = [0] * n   # marks which rows must become 0
    col = [0] * m   # marks which columns must become 0

    # Step 1: mark rows and columns that contain a 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    # Step 2: set cell to 0 if its row or column was marked
    for i in range(n):
        for j in range(m):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0

    return matrix


print("Better:", set_zeroes_better(copy.deepcopy(matrix)))


# ---------- OPTIMAL SOLUTION ----------
# We solve this using the first row and first column
# of the matrix ITSELF as marker arrays, instead of
# creating separate row[]/col[] arrays.
# This removes the O(n+m) extra space used in Better approach.
#
# col0 -> separate flag needed because matrix[0][0] is shared
#         between row marker and column marker
#
# Time Complexity: O(n*m)
# Space Complexity: O(1)

def set_zeroes_optimal(matrix):
    n = len(matrix)
    m = len(matrix[0])
    col0 = 1  # tracks if first column needs to be zeroed

    # Step 1: use first row and first column as markers
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0        # mark row using first column
                if j != 0:
                    matrix[0][j] = 0     # mark column using first row
                else:
                    col0 = 0             # special case for column 0

    # Step 2: use markers to set 0s (process from bottom-right
    # to top-left so we don't overwrite markers before using them)
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if j != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            else:
                if matrix[i][0] == 0 or col0 == 0:
                    matrix[i][j] = 0

    return matrix


print("Optimal:", set_zeroes_optimal(copy.deepcopy(matrix)))