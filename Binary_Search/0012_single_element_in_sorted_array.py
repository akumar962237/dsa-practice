
class Solution:
      # Function to find the single non-duplicate element using binary search
    def singleNonDuplicate(self, arr):
        # Get the size of the array
        n = len(arr)

        # Edge case: only one element in the array
        if n == 1:
            return arr[0]

        # Edge case: first element is the unique one
        if arr[0] != arr[1]:
            return arr[0]

        # Edge case: last element is the unique one
        if arr[n - 1] != arr[n - 2]:
            return arr[n - 1]

        # Initialize binary search bounds
        low, high = 1, n - 2

        # Perform binary search
        while low <= high:
            # Calculate middle index
            mid = (low + high) // 2

            # Check if middle element is the unique one
            if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
                return arr[mid]

            # If mid is in the left half (pairing is valid)
            if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or \
               (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
                # Move to the right half
                low = mid + 1
            else:
                # Move to the left half
                high = mid - 1

        # Dummy return (not reachable if input is valid)
        return -1

# Driver code
if __name__ == "__main__":
    # Input array with all elements appearing twice except one
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

    # Create an object of Solution class
    obj = Solution()

    # Call the function and store the result
    ans = obj.singleNonDuplicate(arr)

    # Print the result
    print("The single element is:", ans)