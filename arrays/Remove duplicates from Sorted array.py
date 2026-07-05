arr = [1,1,2,2,3,4,4,5]

def remove_duplicates(arr):
    write_index = 1
    for read_index in range(1, len(arr)):
        if arr[read_index] != arr[read_index - 1]:
            arr[write_index] = arr[read_index]
            write_index += 1
    return write_index  
result = remove_duplicates(arr) 
print("The length of the array after removing duplicates is:", result)