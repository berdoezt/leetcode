'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
'''
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        val = None
        count = 0

        for i in range(n):
            count += 1
            if val == None:
                val = nums[i]

            if nums[i] > val:
                val = nums[i]
            
            if i + val >= n - 1:
                count += 1
                return count
            
            val -= 1

s = Solution()

# nums = [2,3,1,1,4]
# result = s.jump(nums)
# print(result)
# assert result == 2

nums = [2,3,1,1,4]
result = s.jump(nums)
assert result == 2

nums = [2,0,1]
result = s.jump(nums)
assert result == 1

nums = [5]
result = s.jump(nums)
assert result == 0

nums = [1,2,1,1,1]
result = s.jump(nums)
assert result == 3

# [1,2,5,1,0,0,4]