'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''

class Solution:
    def isIsomorphic(self, s, t) -> bool:
        ms = {}
        mt = {}

        for i in range(len(s)):
            if s[i] not in ms:
                ms[s[i]] = i
            
            if t[i] not in mt:
                mt[t[i]] = i

            if ms[s[i]] != mt[t[i]]:
                return False
            
            ms[s[i]] = i
            mt[t[i]] = i
        
        return True
        

s = Solution()

ss = "egg"
t = "add"
result = s.isIsomorphic(ss, t)
assert result == True

ss = "foo"
t = "bar"
result = s.isIsomorphic(ss, t)
assert result == False

ss = "paper"
t = "title"
result = s.isIsomorphic(ss, t)
assert result == True

ss = "bbbaaaba"
t = "aaabbbba"
result = s.isIsomorphic(ss, t)
assert result == False

ss = "papap"
t = "titii"
result = s.isIsomorphic(ss, t)
assert result == False

ss = "badc"
t = "baba"
result = s.isIsomorphic(ss, t)
assert result == False