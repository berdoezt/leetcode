'''
Given an array arr[] of size n containing integers. The problem is to find the length of the longest sub-array having sum equal to the given value k.

Examples: 

Input: arr[] = { 10, 5, 2, 7, 1, 9 }, k = 15
Output: 4
Explanation: The sub-array is {5, 2, 7, 1}.

Input: arr[] = {-5, 8, -14, 2, 4, 12}, k = -5
Output: 5

[ . . . .. .  . . . .  .]
 [   A    ][     B      ]

A + B = sum
A = sum - B
B = sum - A
'''

class Solution:
    def longest(self, arr, k):
        # time complexity : O(n^2)
        # space complexity : O(1)
        # m = 0
        # for i in range(len(arr)):
        #     sum = 0
        #     for j in range(i, len(arr)):
        #         sum += arr[j]
        #         if sum == k:
        #             size = j - i
        #             if size > m:
        #                 m = size
        
        # return m + 1


        # ===============================================================


        # if all positive number
        # can use sliding window 2 pointer i and j
        # time complexity : O(n)
        # space complexity : O(1)
        # i = 0
        # j = i
        # total = 0
        # m = 0

        # while True:
        #     if i > j:
        #         break

        #     if total < k:
        #         if j == len(arr):
        #             break

        #         total += arr[j]
        #         j += 1
        #     else:
        #         if total == k:
        #             size = j - i
        #             if size > m:
        #                 m = size
                
        #         total -= arr[i]
        #         i += 1

        # return m




        # ===============================================================

        # if containing negative number
        # time complexity : O(n)
        # space complexity : O(n)
        m = {0: -1}
        prefix_sum = 0
        max_length = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]
            if prefix_sum not in m: # for case have zero like [2,0,0,3] k = 3
                m[prefix_sum] = i

            remain_sum = prefix_sum - k
            if remain_sum in m:
                index = m[remain_sum]
                length = i - index
                if length > max_length:
                    max_length = length
        
        return max_length



s = Solution()

assert 4 == s.longest([10, 5, 2, 7, 1, 9 ], k = 15)
assert 3 == s.longest([1,2,3,1,1,1,1,4,2,3], k = 3)
# assert 5 == s.longest([-5, 8, -14, 2, 4, 12], k = -5)
assert 3 == s.longest([2,0,0,3], k = 3)
