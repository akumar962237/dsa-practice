class Solution:
    # Function to count subarrays with given XOR
    def countSubarrays(self, A, k):
        # Store frequency of prefix XORs
        freq = {0: 1}
        
        # Current prefix XOR
        prefixXor = 0
        # Answer count
        count = 0

        # Traverse array
        for num in A:
            # Update prefix XOR
            prefixXor ^= num

            # Compute required XOR
            target = prefixXor ^ k

            # If target exists in map, add its frequency
            if target in freq:
                count += freq[target]

            # Store current prefix XOR in map
            freq[prefixXor] = freq.get(prefixXor, 0) + 1

        return count


# Driver code
A = [4, 2, 2, 6, 4]
k = 6
sol = Solution()
print(sol.countSubarrays(A, k))