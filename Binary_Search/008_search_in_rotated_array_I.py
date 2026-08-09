def search(arr,target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # Check if the left half is sorted
        if arr[low] <= arr[mid]:
            # Target is in the left half
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Right half is sorted
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1  # Target not found
print(search([4,5,6,7,0,1,2], 0))  # Output: 4
print(search([4,5,6,7,0,1,2], 3))  # Output: -1