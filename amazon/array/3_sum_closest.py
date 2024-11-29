# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2967/


class Solution:
    # idea is similar to 3 sum problem, we use two pointer approach
    # time complexity = O(n^2), for every element, we iterate with two pointers technique. for sorting can be O(n log n)
    # space complexity = depend on the sort algo, can be O(log n) to O(n)
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        r = None

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[left] + nums[right] + nums[i]
                abs_diff = abs(target - s)
                if r == None:
                    r = s
                elif abs_diff < abs(target - r):
                    r = s
                
                if s > target:
                    right -= 1
                else:
                    left += 1
        
        return r

        pass

s = Solution()

nums = [-1,2,1,-4]
target = 1
result = s.threeSumClosest(nums, target)
print(result)
assert result == 2

nums = [0,0,0]
target = 1
result = s.threeSumClosest(nums, target)
print(result)
assert result == 0