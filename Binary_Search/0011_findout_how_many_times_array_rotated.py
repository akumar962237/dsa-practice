class Solution:
    # Function to find rotation count using binary search
    def findRotations(self, arr):
        low = 0
        high = len(arr) - 1

        # Loop until low meets high
        while low < high:
            mid = low + (high - low) // 2

            # If mid element is greater than element at high,
            # smallest element lies to the right of mid
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                # Else smallest element is at mid or to the left
                high = mid

        # When low == high, we found the smallest element
        return low

# Driver code
if __name__ == "__main__":
    arr = [4,5,6,7,0,1,2,3]
    sol = Solution()
    rotations = sol.findRotations(arr)
    print(rotations)