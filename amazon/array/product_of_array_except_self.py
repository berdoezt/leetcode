# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/499/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pass

s = Solution()

nums = [1,2,3,4]
result = s.productExceptSelf(nums)
print(result)
assert result == [24,12,8,6]

nums = [-1,1,0,-3,3]
result = s.productExceptSelf(nums)
print(result)
assert result == [0,0,9,0,0]