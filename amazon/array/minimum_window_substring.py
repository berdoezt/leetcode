# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/902/

class Solution:
    # idea is using sliding window
    # TLE
    def contain(self, l: str, t: str) -> bool:
        mt = {}
        for i in t:
            if i not in mt:
                mt[i] = 1
            else:
                mt[i] += 1

        for i in l:
            if i in mt:
                mt[i] -= 1
        
        for i in mt:
            if mt[i] > 0:
                return False
        
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        right = -1
        size_ans = len(s) + 1
        ans = ""
        h = ""

        while True:
            if self.contain(ans, t):
                if len(ans) < size_ans:
                    size_ans = len(ans)
                    h = ans

                if len(ans) == t:
                    return ans

                ans = ans[1:]
            else:
                right += 1
                if right == len(s):
                    break

                ans += s[right]

        return h

class Solution2:
    # https://www.youtube.com/watch?v=jSto0O4AJbM
    # idea is we count the occurence of each letter in word t
    # and then iterate over s, count the letter each
    # if its same, we stop iterate (while have == need) and start shrinking
    # we do it over and over until we found the minimum of length
    # time complexity : O(n + m)
    # space complexity : O(n)
    def minWindow(self, s: str, t: str) -> str:
        mt = {}
        ms = {}

        for i in t:
            if i not in mt:
                mt[i] = 1
            else:
                mt[i] += 1

            if i not in ms:
                ms[i] = 0

        need = len(t)
        have = 0

        idx = []
        length = len(s) + 2

        left = 0
        for i in range(len(s)):
            if s[i] in ms:
                ms[s[i]] += 1

                if ms[s[i]] <= mt[s[i]]:
                    have += 1
            
            while have == need:
                if i - left < length:
                    idx = [left, i]
                    length = i - left

                if s[left] in ms:
                    ms[s[left]] -= 1

                    if ms[s[left]] < mt[s[left]]:
                        have -= 1
                
                left += 1

        if len(idx) == 0:
            return ""   

        return s[idx[0]:idx[1]+1]

s = Solution2()

strs = "ADOBECODEBANC"
t = "ABC"
result = s.minWindow(strs,t)
print(result)
assert result == "BANC"

strs = "a"
t = "a"
result = s.minWindow(strs,t)
print(result)
assert result == "a"

strs = "abc"
t = "abc"
result = s.minWindow(strs,t)
print(result)
assert result == "abc"

strs = "cab"
t = "abc"
result = s.minWindow(strs,t)
print(result)
assert result == "cab"

strs = "cab"
t = "xyz"
result = s.minWindow(strs,t)
print(result)
assert result == ""

strs = "b"
t = "a"
result = s.minWindow(strs,t)
print(result)
assert result == ""

strs = "cabwefgewcwaefgcf"
t = "cae"
result = s.minWindow(strs,t)
print(result)
assert result == "cwae"



# A : 0
# B : 0
# C : 0

# ADOBECODEBANC
# l    ^

