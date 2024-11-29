'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107


[1 1 1]

'''

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # brute force solution
        # time complexity = O(n^2)
        # space complexity = O(1)
        # count = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             count += 1
        #         pass
        
        # return count

        # ===================================


        # optimal solution
        # time complexity = O(n)
        # space complexity = O(n)
        m = {0: 1}
        count = 0
        prefix_sum = 0

        for i in nums:
            prefix_sum += i 

            remain_sum = prefix_sum - k
            if remain_sum in m:
                count += m[remain_sum]
            
            if prefix_sum in m:
                m[prefix_sum] += 1
            else:
                m[prefix_sum] = 1
        
        print(m)
        return count


s = Solution()

nums = [1,1,1]
k = 2
assert s.subarraySum(nums, k) == 2

nums = [1,2,3]
k = 3
assert s.subarraySum(nums, k) == 2

nums = [1,2,3, -3, 1, 1, 1, 4, 2, -3]
k = 3
assert s.subarraySum(nums, k) == 8