'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        i = 0
        j = i
        mp = {}
        longest = 0
        toRemove = []

        while True:
            if j == len(s):
                break

            if s[j] in mp:
                if len(mp) > longest:
                    longest = len(mp)
                
                locationDuplicate = mp[s[j]]
                for k in mp:
                    if mp[k] <= locationDuplicate:
                        toRemove.append(k)

                for k in toRemove:
                    del mp[k]
                

                toRemove = []
                mp[s[j]] = j
            else:
                mp[s[j]] = j


            j += 1
            pass

        if len(mp) > longest:
            longest = len(mp)

        return longest

s = Solution()

st = "abcabcbb"
result = s.lengthOfLongestSubstring(st)
assert result == 3

st = "bbbbb"
result = s.lengthOfLongestSubstring(st)
assert result == 1

st = "pwwkew"
result = s.lengthOfLongestSubstring(st)
assert result == 3

st = " "
result = s.lengthOfLongestSubstring(st)
assert result == 1

st = "au"
result = s.lengthOfLongestSubstring(st)
assert result == 2