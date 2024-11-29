class Solution:
    # idea is to just sort the combined list and then find the median
    # time complexity : O(N log N), N = # of element in array
    # space complexity : O(N)
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        for i in nums2:
            nums1.append(i)
        
        nums1 = sorted(nums1)
        len_nums1 = len(nums1)
        if len_nums1 % 2 == 0:
            right = int(len_nums1 / 2)
            left = right - 1
            return (nums1[left] + nums1[right]) / 2
        
        return nums1[int(len_nums1 / 2)]
        pass

s = Solution()

nums1 = [1,3]
nums2 = [2]
result = s.findMedianSortedArrays(nums1, nums2)
print(result)
assert result == 2.00000

nums1 = [1,2]
nums2 = [3,4]
result = s.findMedianSortedArrays(nums1, nums2)
print(result)
assert result == 2.50000
