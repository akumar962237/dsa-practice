class Solution:
    # Function to find N-th root of M using binary search
    def nthRoot(self, n, m):
        # Set low and high for binary search
        low, high = 1, m

        # Start binary search
        while low <= high:
            # Calculate mid
            mid = (low + high) // 2

            # Store result of mid^n
            ans = 1
            for _ in range(n):
                ans *= mid
                if ans > m:
                    break

            # If mid^n equals m
            if ans == m:
                return mid

            # If mid^n is less than m
            if ans < m:
                low = mid + 1

            # If mid^n is more than m
            else:
                high = mid - 1

        # Return -1 if not found
        return -1

# Driver code
obj = Solution()
result = obj.nthRoot(3, 27)

print(result)