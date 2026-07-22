class Solution(object):
    def isPalindrome(self, x):
        s = str(x)

        if s == s[::-1]:
            return True
        else:
            return False
            
        