'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''

class Solution:
    def trap(self, height: list[int]) -> int:
        result = 0

        highestIndex = None
        secondHighestIndex = None
        for i in range(len(height)):
            if highestIndex == None:
                highestIndex = i
                continue
            
            if secondHighestIndex == None:
                secondHighestIndex = i
                continue

            

        return result

s = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = s.trap(height)
print(result)
assert result == 6

height = [4,2,0,3,2,5]
result = s.trap(height)
assert result == 9
        