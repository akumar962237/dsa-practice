arr = [1, 2, 3, 5, 6]
#----------------------BRUTE FORCE APPROACH-----------------
def missing_number(arr):

    # Total numbers should be 1 to N
    n = len(arr) + 1

    # Check every number from 1 to N
    for i in range(1, n + 1):

        # Assume the number is not found
        found = False

        # Search the current number in the array
        for j in range(len(arr)):

            # If the number is found
            if arr[j] == i:
                found = True
                break

        # If the number is still not found,
        # then it is the missing number
        if not found:
            return i
print(missing_number(arr))



#-----------OPTIMAL APPROACH-----------------
def missing_number(arr):
    n = len(arr) + 1  # Total numbers should be n+1
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    arr_sum = sum(arr)  # Sum of elements in the array
    return total_sum - arr_sum  # The missing number

print(missing_number(arr))
