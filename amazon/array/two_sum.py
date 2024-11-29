'''
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/508/
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        m = {}

        for i in range(len(nums)):
            if target - nums[i] in m:
                return [i, m[target-nums[i]]]
            
            m[nums[i]] = i
        pass

s = Solution()

nums = [2,7,11,15]
target = 9
result = s.twoSum(nums, target)
print(result)
assert result == [1, 0]