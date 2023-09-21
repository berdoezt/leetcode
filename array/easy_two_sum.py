'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
class Solution:
    # complexity : O(n)
    # space : O(n) because of extra map
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        loc = {}
        for i in range(len(nums)):
            if loc.get(target - nums[i]) != None:
                return [i, loc[target-nums[i]]]
            else:
                loc[nums[i]] = i
            pass

        return

s = Solution()

print(s.twoSum([2, 7, 11, 15], 22))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
