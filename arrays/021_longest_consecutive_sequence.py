#------------------------
#   BRUTE FORCE APPROACH
#------------------------

arr = [102,4,100,1,101,3,2,1,1]

def ls(arr, target):
    for num in arr:
        if num == target:
            return True
    return False

def longest_seq_brute(arr):

    if len(arr) == 0:
        return 0

    longest = 1

    for i in range(len(arr)):
        x = arr[i]
        count = 1

        while ls(arr, x + 1):
            x += 1
            count += 1

        longest = max(longest, count)

    return longest

print(longest_seq_brute(arr))


#--------------BETTER APPROACH------------
def longestSuccessiveElements(nums):

    if len(nums) == 0:
        return 0

    nums.sort()

    n = len(nums)

    lastSmaller = float("-inf")
    cnt = 0
    longest = 1

    for i in range(n):

        if nums[i] - 1 == lastSmaller:
            cnt += 1
            lastSmaller = nums[i]

        elif lastSmaller != nums[i]:
            cnt = 1
            lastSmaller = nums[i]

        longest = max(longest, cnt)

    return longest


nums = [100, 102, 100, 101, 101, 4, 3, 2, 3, 2, 1, 1, 1, 2]

print(longestSuccessiveElements(nums))