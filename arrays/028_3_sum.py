# Class to solve 3-sum problem
class Solution:
    # Function to find triplets with sum zero
    def threeSum(self, arr, n):
        # Sort the array
        arr.sort()
        # Store final result
        ans = []

        # First loop for first element
        for i in range(n):
            # Skip duplicates for first element
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            # Two pointers
            left, right = i + 1, n - 1

            # Find pairs for current arr[i]
            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total == 0:
                    ans.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return ans

# Driver code
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    n = len(arr)
    obj = Solution()
    res = obj.threeSum(arr, n)
    for triplet in res:
        print(triplet)