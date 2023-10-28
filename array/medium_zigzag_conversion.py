'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
                             PAHNALIGYIR

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        row = numRows
        backRow = 1
        result = ""

        for i in range(numRows):
            j = i
            counter = 0
            firstHop = (row - 1) * 2
            secondHop = (backRow - 1) * 2
            hops = [firstHop, secondHop]

            while True:
                if j >= len(s):
                    break
                result += s[j]
                hop = hops[counter % 2]
                if hop == 0:
                    hop = hops[(counter + 1) % 2]

                j += hop
                counter += 1
            
            row -= 1
            backRow += 1
            
        return result

ss = Solution()

s = "PAYPALISHIRING"
numRows = 3
result = ss.convert(s, numRows)
assert result == "PAHNAPLSIIGYIR"

s = "PAYPALISHIRING"
numRows = 4
result = ss.convert(s, numRows)
assert result == "PINALSIGYAHRPI"

s = "PAYPALISHIRING"
numRows = 5
result = ss.convert(s, numRows)
assert result == "PHASIYIRPLIGAN"

s = "ALBERT"
numRows = 2
result = ss.convert(s, numRows)
assert result == "ABRLET"

s = "A"
numRows = 1
result = ss.convert(s, numRows)
assert result == "A"
