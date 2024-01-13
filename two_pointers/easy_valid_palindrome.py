'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''



class Solution:

    def isPalindrome(self, s: str) -> bool:
        dict = 'abcdefghijklmnopqrstuvwxyz1234567890'
        i = 0
        j = len(s) - 1

        while True:
            if i >= j:
                return True
            
            while True:
                if i >= j:
                    return True
                
                if s[i].lower() in dict:
                    break

                i += 1
            
            front = s[i].lower()
            
            while True:
                if i >= j:
                    return True
                
                if s[j].lower() in dict:
                    break

                j -= 1    

            back = s[j].lower()

            if front != back:
                return False
            
            i += 1
            j -= 1

s = Solution()

w = "A man, a plan, a canal: Panama"
result = s.isPalindrome(w)
assert result == True

w = "race a car"
result = s.isPalindrome(w)
assert result == False

w = " "
result = s.isPalindrome(w)
assert result == True

w = ".,"
result = s.isPalindrome(w)
assert result == True

w = "abba"
result = s.isPalindrome(w)
assert result == True

w = "abcba"
result = s.isPalindrome(w)
assert result == True