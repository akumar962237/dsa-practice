class UpperBoundFinder:
    # Function to find the upper bound index using binary search
    def upper_bound(self, arr, x):
        low, high = 0, len(arr) - 1     # Search range
        ans = len(arr)                  # Default value if not found

        while low <= high:
            mid = (low + high) // 2     # Find middle index
            if arr[mid] > x:
                ans = mid               # Store possible answer
                high = mid - 1          # Move to the left
            else:
                low = mid + 1           # Move to the right
        return ans                      # Return result

# Driver code
arr = [3, 5, 8, 15, 19]                # Sorted input array
x = 9                                  # Target value

finder = UpperBoundFinder()           # Create object
ind = finder.upper_bound(arr, x)      # Call method

print("The upper bound is the index:", ind)  # Output result