import math

class SmallestDivisorFinder:
    # Helper method to calculate sum by divisor
    def sumByD(self, arr, div):
        return sum(math.ceil(x / div) for x in arr)

    # Method to find the smallest divisor using binary search
    def smallestDivisor(self, arr, limit):
        if len(arr) > limit:
            return -1

        low = 1
        high = max(arr)

        while low <= high:
            mid = (low + high) // 2
            if self.sumByD(arr, mid) <= limit:
                high = mid - 1  # Try smaller divisor
            else:
                low = mid + 1   # Try larger divisor

        return low

# Driver code
solver = SmallestDivisorFinder()
arr = [1, 2, 3, 4, 5]
limit = 8
print("The minimum divisor is:", solver.smallestDivisor(arr, limit))