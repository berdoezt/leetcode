'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
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
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = []
        m = {}

        for i in strs:
            if result == []:
                result.append([i])
                continue
            
            found = False
            for j in range(len(result)):
                if self.isAnagram(i, result[j][0]):
                    result[j].append(i)
                    found = True
            
            if found == False:
                result.append([i])
            
        return result
        pass

s = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
result = s.groupAnagrams(strs)
print(result)
# assert result == [["bat"],["nat","tan"],["ate","eat","tea"]]