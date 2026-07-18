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