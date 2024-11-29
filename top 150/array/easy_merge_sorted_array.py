'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

'''
class Solution:
    # complexity : O(m + n)
    # space : O(1)
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n == 0:
            return
        
        o = m + n
        
        for i in range(m - 1, -1, -1):
            nums1[i], nums1[o - 1] = nums1[o - 1], nums1[i]
            o -= 1

        i = n
        j = 0
        k = 0

        while 1:
            if k == m + n:
                break

            if i >= m + n:
                nums1[k] = nums2[j]
                j += 1
            elif j >= n:
                pass 
            elif nums1[i] < nums2[j]:
                nums1[i], nums1[k] = nums1[k], nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        pass

s = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s.merge(nums1, m, nums2, n)
assert nums1 == [1,2,2,3,5,6]

nums1 = [1,2,0,0,0,0]
m = 2
nums2 = [3,4,5,6]
n = 4
s.merge(nums1, m, nums2, n)
assert nums1 == [1,2,3,4,5,6]

nums1 = [1]
m = 1
nums2 = []
n = 0
s.merge(nums1, m, nums2, n)
assert nums1 == [1]

nums1 = [0]
m = 0
nums2 = [1]
n = 1
s.merge(nums1, m, nums2, n)
assert nums1 == [1]