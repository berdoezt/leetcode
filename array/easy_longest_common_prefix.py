'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution:
    # complexity : O(n^2)
    # space : O(1)
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 0
        result = ""
        while True:
            c = None
            for s in strs:
                if i >= len(s):
                    return result
                
                if c == None:
                    c = s[i]
                    continue

                if s[i] != c:
                    return result
            
            result += strs[0][i]

            i += 1

s = Solution()

strs = ["flower","flow","flight"]
result = s.longestCommonPrefix(strs)
assert result == "fl"

strs = ["dog","racecar","car"]
result = s.longestCommonPrefix(strs)
assert result == ""