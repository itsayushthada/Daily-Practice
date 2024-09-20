class Solution:

    def expandFromMiddle(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        return (right - 1) - (left + 1) + 1

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1 or s == s[::-1]:
            return s

        max_len = 0
        left, right = 0, 0

        for i in range(len(s)):
            len_1 = self.expandFromMiddle(s, i, i) # Odd Polynomial
            len_2 = self.expandFromMiddle(s, i, i+1) # Even Polynomial

            if len_1 > max_len and len_1 > len_2:
                max_len = len_1
                left, right = i - len_1//2, i + len_1//2
            elif len_2 > max_len and len_2 >= len_1:
                max_len = len_2
                left, right = i - len_2//2+1, i + len_2//2

            print("after", left, right, s[left:right+1])
        
        return s[left:right+1]
