'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        i = 0
        j = i
        temp = 0
        minLength = len(nums) + 1

        while True:
            if j == len(nums):
                break

            temp += nums[j]
            if temp >= target:
                length = j - i
                if length == 0:
                    return length + 1
                
                if length < minLength:
                    minLength = length
                
                while i <= j:
                    temp -= nums[i]
                    if temp >= target:
                        i += 1
                        length = j - i
                        if length == 0:
                            return length + 1
                        
                        if length < minLength:
                            minLength = length
                    else:
                        i += 1
                        break
            
            j += 1
        
        if minLength == len(nums) + 1:
            return 0
        
        return minLength + 1

s = Solution()

target = 7
nums = [2,3,1,2,4,3]
result = s.minSubArrayLen(target, nums)
assert result == 2

target = 4
nums = [1,4,4]
result = s.minSubArrayLen(target, nums)
assert result == 1

target = 11
nums = [1,1,1,1,1,1,1,1]
result = s.minSubArrayLen(target, nums)
assert result == 0

target = 80
nums = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]
result = s.minSubArrayLen(target, nums)
assert result == 6

