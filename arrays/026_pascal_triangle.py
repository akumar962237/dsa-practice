'''
#Problem 1: Pascal's Triangle I (Find the Element at a Given Position)
Introduction

Given the row number (R) and column number (C) (1-based indexing), find the element present at that position in Pascal's Triangle.

Instead of generating the entire triangle, we directly compute the required element using the Binomial Coefficient (nCr), which is the most optimal approach.

Example
Input:
Row = 5
Column = 3

Output:
'''
# Function to calculate nCr (Binomial Coefficient)
def nCr(n, r):

    # Stores the final answer
    res = 1

    # Compute nCr iteratively to avoid factorial calculations
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)

    return res


# Example Input (1-based indexing)
row = 5
col = 3

# Convert to 0-based indexing and print the required element
print(nCr(row - 1, col - 1))