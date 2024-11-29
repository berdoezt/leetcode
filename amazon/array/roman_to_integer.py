# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2965/

class Solution:
    # iterate all characters
    # if found C, X, I, check for the character after it, because it could be 4xx / 9xx
    # time complexity : O(n)
    # space complexity : O(1)
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            if s[i] == 'M':
                result += 1000
                i += 1
                continue
            
            if s[i] == 'C' and i + 1 < len(s) and s[i+1] == 'M':
                result += 900
                i += 2
                continue

            if s[i] == 'D':
                result += 500
                i += 1
                continue

            if s[i] == 'C' and i + 1 < len(s) and s[i+1] == 'D':
                result += 400
                i += 2
                continue

            if s[i] == 'C':
                result += 100
                i += 1
                continue

            if s[i] == 'X' and i + 1 < len(s) and s[i+1] == 'C':
                result += 90
                i += 2
                continue

            if s[i] == 'L':
                result += 50
                i += 1
                continue

            if s[i] == 'X' and i + 1 < len(s) and s[i+1] == 'L':
                result += 40
                i += 2
                continue

            if s[i] == 'X':
                result += 10
                i += 1
                continue

            if s[i] == 'I' and i + 1 < len(s) and s[i+1] == 'X':
                result += 9
                i += 2
                continue

            if s[i] == 'V':
                result += 5
                i += 1
                continue

            if s[i] == 'I' and i + 1 < len(s) and s[i+1] == 'V':
                result += 4
                i += 2
                continue

            if s[i] == 'I':
                result += 1
                i += 1
                continue

        return result

s = Solution()

st = "III"
result = s.romanToInt(st)
print(result)
assert result == 3

st = "LVIII"
result = s.romanToInt(st)
print(result)
assert result == 58

st = "MCMXCIV"
result = s.romanToInt(st)
print(result)
assert result == 1994

