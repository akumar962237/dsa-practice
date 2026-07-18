"""
Problem: Move All Zeros to End

Approach: Brute Force

"""
'''''
Problem: Move All Zeros to End

Approach: Optimal (Two Pointer)

Algorithm:
1. Find the index of the first zero in the array.
2. If no zero is found, return the original array.
3. Traverse the array from the next index after the first zero.
4. Whenever a non-zero element is found, swap it with the element at the zero index.
5. Move the zero index one step forward after every swap.
6. Continue until the end of the array.

Time Complexity: O(n)
Space Complexity: O(1)
'''

arr = [0, 1, 0, 2, 0, 3, 4, 5]

def move_zeros_optimal(arr):

    zero_index = -1

    # Step 1: Find the first zero
    for i in range(len(arr)):
        if arr[i] == 0:
            zero_index = i
            break

    # If there is no zero, return the original array
    if zero_index == -1:
        return arr

    # Step 2: Move non-zero elements to the first zero position
    for i in range(zero_index + 1, len(arr)):
        if arr[i] != 0:
            arr[zero_index], arr[i] = arr[i], arr[zero_index]
            zero_index += 1

    return arr

print(move_zeros_optimal(arr))