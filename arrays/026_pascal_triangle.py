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

'''

Problem 2: Pascal's Triangle II (Print the Nth Row)
Introduction

Given an integer N, print the Nth row of Pascal's Triangle.

Instead of generating the entire triangle, we generate only the required row using the relation between consecutive binomial coefficients.

This avoids unnecessary computations and is the optimal solution.

Example
Input:
N = 5

Output:
1 4 6 4 1

'''
# Class containing Pascal's Triangle row generation logic
class Solution:

    # Function to generate the Nth row of Pascal's Triangle
    def getNthRow(self, N):

        # List to store the required row
        row = []

        # First element of every row is always 1
        val = 1
        row.append(val)

        # Generate the remaining elements using the previous element
        for k in range(1, N):

            # Compute next value using:
            # C(n,k) = C(n,k-1) * (n-k) / k
            val = val * (N - k) // k

            # Store the computed value
            row.append(val)

        # Return the generated row
        return row


# Example Input
N = 5

# Create object
obj = Solution()

# Print the Nth row
print(*obj.getNthRow(N))


'''
Problem 3: Pascal's Triangle III (Print the Entire Triangle)
Introduction

Given an integer N, print the first N rows of Pascal's Triangle.

Instead of computing every element using factorials or previously generated rows, we generate each row independently using the binomial coefficient relation.

This is the most efficient and commonly accepted solution.

Example
Input:
N = 5

Output:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''


# Class containing Pascal's Triangle generation logic
class Solution:

    # Function to generate a single row
    def generateRow(self, row):

        # List to store the current row
        ans = []

        # First element is always 1
        val = 1
        ans.append(val)

        # Generate remaining elements
        for col in range(1, row):

            # Compute next element using previous one
            val = val * (row - col) // col

            # Store the element
            ans.append(val)

        # Return the generated row
        return ans


    # Function to generate the complete Pascal's Triangle
    def generate(self, N):

        # Stores all rows of the triangle
        triangle = []

        # Generate rows one by one
        for row in range(1, N + 1):

            # Append each generated row
            triangle.append(self.generateRow(row))

        # Return the complete triangle
        return triangle


# Example Input
N = 5

# Create object
obj = Solution()

# Generate Pascal's Triangle
result = obj.generate(N)

# Print the triangle
for row in result:
    print(*row)