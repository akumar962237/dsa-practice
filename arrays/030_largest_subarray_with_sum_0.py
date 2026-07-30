# compute length of the longest subarray with sum 0
def maxLen(A: list[int], n: int) -> int:
    # map prefix sum -> first index seen
    mpp: dict[int, int] = {}
    # best length so far
    maxi = 0
    # running prefix sum
    s = 0

    # iterate over the array
    for i in range(n):
        # update running sum
        s += A[i]

        # if sum is zero, subarray [0..i] has zero sum
        if s == 0:
            # update best length
            maxi = i + 1
        # otherwise check if this sum was seen before
        else:
            # when seen, zero-sum segment between previous index + 1 and i
            if s in mpp:
                # maximize length
                maxi = max(maxi, i - mpp[s])
            # first time seeing this sum
            else:
                # record index
                mpp[s] = i

    # return best length
    return maxi

# program entry
def main():
    # sample input
    A = [9, -3, 3, -1, 6, -5]
    # compute size
    n = len(A)
    # print result
    print(maxLen(A, n))

# run main
if __name__ == "__main__":
    main()