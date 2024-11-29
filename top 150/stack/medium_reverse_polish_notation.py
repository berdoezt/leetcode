'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''

class MinStack:

    def __init__(self):
        self.stack = []
        pass

    def push(self, val: int) -> None:
        self.stack.append(val)
        pass

    def pop(self) -> None:
        self.stack.pop(len(self.stack) - 1)
        pass

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        pass

    def getMin(self) -> int:
        m = None
        for i in self.stack:
            if m == None:
                m = i
                continue
            if i < m:
                m = i
        
        return m
        pass

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s = MinStack()

        operator = ['+', '-', '*', '/']

        for token in tokens:
            if token not in operator:
                s.push(int(token))
            else:
                val2 = s.top()
                s.pop()

                val1 = s.top()
                s.pop()

                if token == "+":
                    s.push(val1 + val2)
                elif token == "-":
                    s.push(val1 - val2)
                elif token == "*":
                    s.push(val1 * val2)
                elif token == "/":
                    s.push(int(val1 / val2))
        
        return s.top()

s = Solution()

tokens = ["2","1","+","3","*"]
assert s.evalRPN(tokens) == 9

tokens = ["4","13","5","/","+"]
assert s.evalRPN(tokens) == 6

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
assert s.evalRPN(tokens) == 22