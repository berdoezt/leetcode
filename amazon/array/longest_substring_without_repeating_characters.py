# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2961/

class Solution1:
    # (bruteforce)
    # check all substring, if unique then check length
    # if length > max length : max length = length
    # time complexity : O(n^3)
    # space complexity : O(n)
    def unique(self, i, j, s):
        m = {}

        for k in range(i, j +1):
            if s[k] in m:
                return False
            
            m[s[k]] = True
        
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        result = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.unique(i, j, s):
                    if j - i > result:
                        result = j - i
        
        return result + 1

class Solution2:
    # sliding window + hashmap
    # i = j = 0 initially
    # j keep running until the end and count the occurence of character
    # every time s[j] frequence > 1, "move" i to the first occurence of s[j] + 1
    # because we have to remove all the characters before first occurence of s[j], because it doesn't make sense to include it
    # example : abcdefghijklmnh
    # when found h again, the only other possible valid substring is start from char 'i' ijklmnh....
    # move pointer i while removing characters before first occurences of s[j] because we won't need it anymore
    # time complexity = O(2n) because each character can be visited by i and j
    # space complexity = O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        i = 0
        m = {}

        result = 0
        for j in range(len(s)):
            if s[j] not in m:
                m[s[j]] = 1
            else:
                m[s[j]] += 1

            while m[s[j]] > 1:
                m[s[i]] -= 1
                i += 1
            
            if j - i > result:
                result = j - i
        
        return result + 1

class Solution3:
    # sliding window + hashmap
    # similar to solution2 but instead of moving i little by little, we can just move i to the next character after first occurence of s[j]
    # if i is greater than the first occurence of s[j], no need to move i, meaning its the character in the past which we no longer need
    # we need to store the index of character and update the index everytime
    # time complexity = O(n) because each character can be visited by j only, i only visit some of it
    # space complexity = O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        i = 0
        m = {}

        result = 0
        for j in range(len(s)):
            if s[j] in m:
                if m[s[j]] >= i:
                    i = m[s[j]] + 1
                
            m[s[j]] = j
            
            if j - i > result:
                result = j - i
        
        return result + 1

sol = Solution3()

s = "abcabcbb"
result = sol.lengthOfLongestSubstring(s)
print(result)
assert result == 3

s = "bbbbb"
result = sol.lengthOfLongestSubstring(s)
print(result)
assert result == 1

s = "pwwkew"
result = sol.lengthOfLongestSubstring(s)
print(result)
assert result == 3


# abcdefghijklmnh...a


# pwwkew
#    l
#      r

# l = 0 1 2 3
# r = 0 1 2 3 4 5
# m = {
#     p: 0,
#     w: 1,
#     k: 1,
#     e: 1
# }
# res = 3

