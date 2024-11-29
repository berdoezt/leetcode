# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2968/

class Solution:
    # idea is to iterate over the haystack
    # starting from i, check if substring of haystack from i to i + len(needle) is equal to needle
    # time complexity: O(n)
    # space complexity: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack)):
            temp = haystack[i:i+len(needle)]
            if temp == needle:
                return i
        
        return -1

s = Solution()

haystack = "sadbutsad"
needle = "sad"
result = s.strStr(haystack, needle)
print(result)
assert result == 0

haystack = "leetcode"
needle = "leeto"
result = s.strStr(haystack, needle)
print(result)
assert result == -1

haystack = "mississippi"
needle = "issip"
result = s.strStr(haystack, needle)
print(result)
assert result == 4