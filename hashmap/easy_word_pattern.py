'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = {}
        ms = {}

        sArr = s.split(" ")
        if len(pattern) != len(sArr):
            return False
                
        for i in range(len(pattern)):
            if pattern[i] not in mp:
                mp[pattern[i]] = i
            
            if sArr[i] not in ms:
                ms[sArr[i]] = i

            if mp[pattern[i]] != ms[sArr[i]]:
                return False
            
            mp[pattern[i]] = i
            ms[sArr[i]] = i
        
        return True
        pass

s = Solution()

pattern = "abba"
ss = "dog cat cat dog"
result = s.wordPattern(pattern, ss)
assert result == True

pattern = "abc"
ss = "b c a"
result = s.wordPattern(pattern, ss)
assert result == True
