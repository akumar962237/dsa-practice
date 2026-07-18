#Brute force approach
arr1 = [1,1,2,3,4,5]
arr2 = [2,2,3,4,6]

def union(arr1,arr2):
    s = set()

    for i in range(len(arr1)):
        s.add(arr1[i])

    for i in range(len(arr2)):
        s.add(arr2[i])

    return sorted(list(s))
print(union(arr1,arr2))

#-----------------------------OPTIMAL APPROACH-----------------------------------------

def union(arr1, arr2):

    # Length of both arrays
    n1 = len(arr1)
    n2 = len(arr2)

    # Two pointers
    i = 0
    j = 0

    # Result array
    result = []

    # Traverse both arrays
    while i < n1 and j < n2:

        # If arr1 element is smaller or equal
        if arr1[i] <= arr2[j]:

            # Add only if it is not already present
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])

            # Move pointer of arr1
            i += 1

        # If arr2 element is smaller
        else:

            # Add only if it is not already present
            if len(result) == 0 or result[-1] != arr2[j]:
                result.append(arr2[j])

            # Move pointer of arr2
            j += 1

    # Add remaining elements of arr1
    while i < n1:

        if len(result) == 0 or result[-1] != arr1[i]:
            result.append(arr1[i])

        i += 1

    # Add remaining elements of arr2
    while j < n2:

        if len(result) == 0 or result[-1] != arr2[j]:
            result.append(arr2[j])

        j += 1

    return result

print(union(arr1, arr2))