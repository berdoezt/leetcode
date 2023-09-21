'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

'''
class Solution:
    # complexity : O(n)
    # space : O(1)
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        result = None
        for i in nums:
            if count == 0:
                result = i
            
            if i == result:
                count += 1
            else:
                count -= 1

        return result

s = Solution()

nums = [3,2,3]
result = s.majorityElement(nums)
assert result == 3

nums = [2,2,1,1,1,2,2]
result = s.majorityElement(nums)
assert result == 2