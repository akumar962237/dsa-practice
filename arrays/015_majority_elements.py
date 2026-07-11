#----------BRUTE FORCE SOLUTION----------
def majority_element_brute_force(nums):
    n = len(nums)
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1
        if count > n // 2:
            return nums[i]
    return -1
nums = [1,1,2,1,3,4,1,2,5,1,1,1]
print(majority_element_brute_force(nums)) 

#---------BETTER SOLUTION USING HASHMAP ----------
def majority_element_hashmap(nums):
    n = len(nums)
    count_map = {}
    for num in nums:
        count_map[num] = count_map.get(num, 0) + 1
    for num, count in count_map.items():
        if count > n // 2:
            return num
    return -1
print(majority_element_hashmap(nums))

#---------OPTIMAL SOLUTION USING MOORE'S VOTING ALGORITHM ----------
def majority_element_moore(nums):
    count = 0
    el = None

    for num in nums:
        if count == 0:
            el = num
        count += (1 if num == el else -1)

    # Verify if the candidate is actually the majority element
    if nums.count(el) > len(nums) // 2:
        return el
    return -1
nums = [1,1,1,1,2,2,2,2,3,3,4,4,1,1,1,1,1]
print(majority_element_moore(nums))