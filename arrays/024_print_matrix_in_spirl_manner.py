def spiralMatrix(matrix):

    # Number of rows
    n = len(matrix)

    # Number of columns
    m = len(matrix[0])

    # Four boundaries
    left = 0
    right = m - 1
    top = 0
    bottom = n - 1

    # Stores the spiral traversal
    ans = []

    # Continue until all boundaries cross
    while top <= bottom and left <= right:

        # -------------------------
        # Traverse Left → Right
        # -------------------------
        for i in range(left, right + 1):
            ans.append(matrix[top][i])

        top += 1

        # -------------------------
        # Traverse Top → Bottom
        # -------------------------
        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])

        right -= 1

        # -------------------------
        # Traverse Right → Left
        # Execute only if rows remain
        # -------------------------
        if top <= bottom:

            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])

            bottom -= 1

        # -------------------------
        # Traverse Bottom → Top
        # Execute only if columns remain
        # -------------------------
        if left <= right:

            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])

            left += 1

    return ans


# Driver Code

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiralMatrix(matrix))