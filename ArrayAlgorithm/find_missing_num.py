"""

Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.

Examples:
    Input: arr[] = {1, 2, 4, 6, 3, 7, 8} , N = 8
    Output: 5
    Explanation: Here the size of the array is 8, so the range will be [1, 8]. The missing number between 1 to 8 is 5

    Input: arr[] = {1, 2, 3, 5}, N = 5
    Output: 4
    Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4

"""

def solution1(arr, N):
    """Finding the missing number

    Args:
        arr (list): input list
        N: length of array
    """
    # real sum of array
    sum_arr = sum(arr)
    # expected sum of array
    expected_sum = (N * (N+1)) // 2

    return expected_sum - sum_arr

def solution2(arr, N):
    """Finding the missing number

    Args:
        arr (list): input list
        N: length of array
    """
    # create hash array of size n+1
    hash = [0] * (N + 1)
    # store frequencies of elements
    for ele in arr:
        hash[ele] += 1

    # finding missing number
    for i in range(1, N+1):
        if hash[i] == 0:
            return i
    
    # edge case handling (though problem guarantees a solution)
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 5]

    res1 = solution1(arr, 5)
    print('Missing number is: \n')
    print(res1)

    res2 = solution2(arr, 5)
    print('Missing number is: \n')
    print(res2)