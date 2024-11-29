# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2970/

class Solution:
    # idea is since anagram will have same letters in words, we will sort the word and put it as hash key
    # then to put it on the same group, we will check the sorted one and check if the group hash already created
    # if created, put it with others, otherwise create new group
    # time complexity = O(n * k log k), n is length of strs, k is length of a string in strs. Sorting can take O(n log n)
    # space complexity = O(nk) the total data to store in result
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        m = {}

        for i in strs:
            s = "".join(sorted(i))

            if s not in m:
                m[s] = [i]
            else:
                m[s].append(i)
        
        result = []

        for i in m:
            result.append(m[i])

        return result

s = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
result = s.groupAnagrams(strs)
print(result)

strs = [""]
result = s.groupAnagrams(strs)
print(result)

strs = ["a"]
result = s.groupAnagrams(strs)
print(result)

