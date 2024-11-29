'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

'''
class Solution:
    # complexity : O(n)
    # space : O(n)
    # def rotate(self, nums: list[int], k: int) -> None:
    #     temp = []
    #     for i in range(len(nums)):
    #         temp.append(None)
        
    #     for i in range(len(nums)):
    #         temp[(i + k) % len(nums)] = nums[i]
        
    #     for i in range(len(nums)):
    #         nums[i] = temp[i]

    
    def rotate(self, nums: list[int], k: int) -> None:
        # complexity : O(n)
        # space : O(1)
        x = k % len(nums)

        # [1,2,3,4,5,6,7]

        for i in range(int(len(nums) / 2)):
            nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]
        
        # [7,6,5,4,3,2,1]
        
        for i in range(int(x / 2)):
            nums[i], nums[x - i - 1] = nums[x - i - 1], nums[i]

        # [5,6,7,4,3,2,1]
        
        for i in range(int((len(nums) - x) / 2)):
            nums[x + i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[x + i]
        
        # [5,6,7,1,2,3,4]
        pass



s = Solution()

nums = [1,2,3,4,5,6,7]
s.rotate(nums, 3)
assert nums == [5,6,7,1,2,3,4]

nums = [-1,-100,3,99]
s.rotate(nums, 2)
assert nums == [3,99,-1,-100]