# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2966/

class Solution:
    # we only need the value, so its easier to sort the value first to skip duplicate
    # we iterate the sorted arrays, and find the 0 maker for the element using two pointer approach, 
    # left and right point to element after and last element
    # check if the sum of left and right equals to target, put all value in result
    # if less than target, move forward the letf, otherwise move backward the right
    # handle duplicate element is relatively easy because the same element will be next to each other
    # time complexity : O(n^2), 
    #   the sort cost O(n log n)
    #   for every element, we access it again hence O(n^2)
    #   total is O(n log n + n^2) -> asymtotically equals to O(n^2)
    # space complexity : from O(log n) to O(n) depend on the sort algorithm
    #   we skip the space for storing the result
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
    
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            target = 0 - nums[i]
            while (left < right):
                if left - 1 != i and nums[left] == nums[left -1]:
                    left += 1
                    continue

                temp = nums[left] + nums[right]
                if  temp == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif temp < target:
                    left += 1
                else:
                    right -= 1
            
        return result

class Solution2:
    # what if we can't do sort ?
    # idea is we can utilize the solution from two sum problem. 
    # we use hashmap m to track if we ever counter the value
    # for every element, that should be the target for the rest forward of the other elements
    # to store the result r, we use set because we want to maintain the uniqueness of the result
    # to avoid TLE, we also check in dup
    # time complexity : O(n^2)
    # space complexity: O(n)

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        r = set()
        dup = {}
        for i in range(len(nums)):
            if nums[i] not in dup:
                dup[nums[i]] = True
                target = -nums[i]

                m = {}

                temp = nums[i+1:]

                for j in range(len(temp)):
                    if target - temp[j] in m:
                        r.add(tuple(sorted([temp[j], target-temp[j], nums[i]])))

                    m[temp[j]] = j

        return r

s = Solution2()

nums = [-1,0,1,2,-1,-4]
result = s.threeSum(nums)
print(result)

nums = [-2,0,0,2,2]
result = s.threeSum(nums)
print(result)

nums = [3,0,-2,-1,1,2]
result = s.threeSum(nums)
print(result)

nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
result = s.threeSum(nums)
print(result)