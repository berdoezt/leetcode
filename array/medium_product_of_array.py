'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
class Solution:
    # complexity : O(n)
    # space : O(n)
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        zero = []
        total = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                if len(zero) != 0:
                    total *= 0
                else:
                    total *= 1

                zero.append(i)
            else:
                total *= nums[i]
        
        for i in range(len(nums)):
            if len(zero) == 0:
                result.append(int(total / nums[i]))
            elif len(zero) == 1:
                if nums[i] != 0:
                    result.append(0)
                else:
                    result.append(total)
            else:
                result.append(0)
        
        return result

s = Solution()

nums = [1,2,3,4]
result = s.productExceptSelf(nums)
assert result == [24,12,8,6]

nums = [-1,1,0,-3,3]
result = s.productExceptSelf(nums)
assert result == [0,0,9,0,0]

nums = [-1,1,0,-3,0]
result = s.productExceptSelf(nums)
assert result == [0,0,0,0,0]
