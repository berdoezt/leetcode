# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2964/

class Solution:
    # loop until 0
    def intToRoman(self, num: int) -> str:
        result = ""
        m = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        while num > 0:
            for i in m:
                if num >= i:
                    result += m[i]
                    num -= i
                    break
                else:
                    continue
                 
        return result

s = Solution()

num = 3749
result = s.intToRoman(num)
print(result)
assert result == "MMMDCCXLIX"

num = 58
result = s.intToRoman(num)
print(result)
assert result == "LVIII"
