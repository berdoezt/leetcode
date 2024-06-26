'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            "{": "}",
            "[": "]",
            "(": ")",
        }
        stack = []

        for i in s:
            if len(stack) == 0:
                stack.append(i)
                continue

            if i in parentheses:
                stack.append(i)
            else:
                if stack[len(stack)-1] in parentheses and i == parentheses[stack[len(stack) - 1]]:
                    stack.pop(len(stack) - 1)
                else:
                    stack.append(i)
        
        return len(stack) == 0

s = Solution()

assert s.isValid("()") == True
