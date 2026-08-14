class Solution:
    # Function to find a peak element using binary search
    def findPeakElement(self, nums):
        # Set left and right bounds
        low, high = 0, len(nums) - 1

        # Binary search loop
        while low < high:
            # Find mid point
            mid = (low + high) // 2

            # If mid element is greater than next
            if nums[mid] > nums[mid + 1]:
                # Move to left half
                high = mid
            else:
                # Move to right half
                low = mid + 1

        # Return peak index
        return low

# Input array
nums = [1, 2, 1, 3, 5, 5, 4]

# Create object
obj = Solution()

# Output result
print(obj.findPeakElement(nums))