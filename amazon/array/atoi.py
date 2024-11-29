'''
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2962/
'''

class Solution:
    def ret(self, isNegative, result):
        r = result
        if isNegative:
            r = -1*result
        
        if r > 2147483647:
            return 2147483647
        
        if r < -2147483648:
            return -2147483648
        
        return r
    
    def myAtoi(self, s: str) -> int:
        result = 0
        digits = '0123456789'
        isNegative = False
        idx = -1
        for i in range(len(s)):
            if s[i] == ' ':
                idx = i
            else:
                break
       
        idx += 1

        for i in range(idx, len(s)):

            if s[i] == '-' and i == idx:
                isNegative = True
                continue

            if s[i] == '+' and i == idx:
                continue
            
            if s[i] not in digits:
                return self.ret(isNegative,result)
            
            result = result*10 + int(s[i])
        return self.ret(isNegative, result)

s = Solution()

result = s.myAtoi("    -042")
print(result)
assert result == -42

result = s.myAtoi("-91283472332")
print(result)
assert result == -2147483648
