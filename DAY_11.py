class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        b = 0
        a = x
        while x > 0:
            digit = x % 10
            b = b * 10 + digit
            x //= 10
        return a == b
