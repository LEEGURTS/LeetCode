class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return [left,right]

        if len(s) < 2 or s == s[::-1]:
            return s
        result = [0,0]
        for i in range(len(s)-1):
            result = max(result,check(i,i+1),check(i,i+2),key = lambda x:(x[1]- x[0]))
        return s[result[0]+1:result[1]]
