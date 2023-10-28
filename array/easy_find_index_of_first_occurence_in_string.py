'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = 0
        res = None
        i = -1
        while True:
            i += 1
            if i == len(haystack):
                return -1
            
            if haystack[i] == needle[j]:
                if j == 0:
                    res = i
                j += 1
            else:
                j = 0
                if res != None:
                    i = res
                    res = None
        
            if j == len(needle):
                return res
        
        

s = Solution()

haystack = "sadbutsad"
needle = "sad"
result = s.strStr(haystack, needle)
assert result == 0

haystack = "leetcode"
needle = "leeto"
result = s.strStr(haystack, needle)
assert result == -1

haystack = "mississippi"
needle = "issip"
result = s.strStr(haystack, needle)
assert result == 4