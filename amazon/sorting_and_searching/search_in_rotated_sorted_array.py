class Solution:
    def search(self, nums: list[int], target: int) -> int:
        len_nums = len(nums)

        left = 0
        right = len_nums - 1

        while left < right:
            mid = int(left + (right - left) / 2)

            if nums[mid]
        pass

s = Solution()

nums = [4,5,6,7,0,1,2]
target = 0
result = s.search(nums, target)
assert result == 4