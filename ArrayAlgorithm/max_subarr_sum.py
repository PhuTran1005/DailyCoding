"""

Given an array arr[], the task is to find the subarray that has the maximum sum and return its sum.

Examples:
    Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
    Output: 11
    Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

    Input: arr[] = {-2, -4}
    Output: –2
    Explanation: The subarray {-2} has the largest sum -2.

    Input: arr[] = {5, 4, 1, 7, 8}
    Output: 25
    Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.

"""

def solution1(arr):
    """Finding the subarray that has the maximum sum

    Args:
        arr (list): input list
    """
    res = arr[0]
    # outer loop for starting point of subarray
    for i in range(len(arr)):
        curr_sum = 0
        # inner loop for ending point of subarray
        for j in range(i, len(arr)):
            curr_sum = curr_sum + arr[j]
            # update res if curr_sum greater than res
            res = max(curr_sum, res)

    return res


if __name__ == '__main__':
    arr = [2, 3, -8, 7, -1, 2, 3]
    res1 = solution1(arr)
    print('Solution 1, naive approach.\n')
    print(res1)