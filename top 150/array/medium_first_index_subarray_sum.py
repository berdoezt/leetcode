'''
Given array and target number. Find the first subarray that sum equals to target number.
Return the pair of first index and last index of the subarray

0 < nums[i] < 10^4
-10^4 < target < 10^4
'''

def solution(arr, target):
    # sliding window
    # two pointer
    # time complexity : O(n) average
    # i = 0
    # j = 0
    # s = arr[j]

    # while True:
    #     if s == target:
    #         return [i, j]
        
    #     if s > target:
    #         s -= arr[i]
    #         i += 1
    #     else:
    #         j += 1
    #         s += arr[j]
        
    #     if i >= len(arr):
    #         return []

    #     if i > j:
    #         j = i
    #         s = arr[j]

    # =================================


    # prefix sum
    # [    ]
    # [A][B]
    # A + B = X
    # time complexity = O(n)
    # space complexity = O(n)
    m = {0: -1}
    prefix_sum = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]
        previous_sum = prefix_sum - target
        if previous_sum in m:
            return [m[previous_sum] + 1, i]
    
        m[prefix_sum] = i

    return []

assert solution([1,2,3], 5) == [1,2]
assert solution([5,2,7,10], 10) == [3,3]
assert solution([10,2,7,10], 10) == [0,0]
assert solution([10,2,7,10], 0) == []
assert solution([0,0,0,0], 0) == [0,0]
assert solution([0,0,0,0], -1) == []
assert solution([1,2,0,3], 0) == [2,2]
assert solution([9, 9, 8, 5, 2], 5) == [3,3]
assert solution([9, 9, 8, 1, 2, 10], 3) == [3,4]