'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}

        for i in magazine:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1

        for i in ransomNote:
            if i not in m:
                return False
            
            m[i] -= 1
            if m[i] == 0:
                del m[i]
            
        return True

s = Solution()

result = s.canConstruct("a", "b")
assert result == False

result = s.canConstruct("aa", "ab")
assert result == False

result = s.canConstruct("aa", "aab")
assert result == True
