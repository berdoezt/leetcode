'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ms = {}
        mt = {}

        for i in s:
            if i not in ms:
                ms[i] = 1
            else:
                ms[i] += 1

        for i in t:
            if i not in mt:
                mt[i] = 1
            else:
                mt[i] += 1
        
        for i in ms:
            if i not in mt:
                return False
            
            if ms[i] != mt[i]:
                return False
        
        for i in mt:
            if i not in ms:
                return False
            
            if ms[i] != mt[i]:
                return False
        
        return True
        pass

s = Solution()

ss = "anagram"
tt = "nagaram"
result = s.isAnagram(ss, tt)
assert result == True

ss = "rat"
tt = "car"
result = s.isAnagram(ss, tt)
assert result == False