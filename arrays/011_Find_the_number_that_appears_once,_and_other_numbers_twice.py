arr = [1,1,2,3,3,4,4,5,5]

#----------------------BRUTE FORCE APPROACH-----------------
def find_single_number(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            return arr[i]
    return None
print(find_single_number(arr))

#----------------------OPTIMAL APPROACH-----------------
def find_single_number(arr):
    XOR = 0
    for i in range(len(arr)):
        XOR ^= arr[i]
    return XOR
print(find_single_number(arr))