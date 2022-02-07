from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        last = 0
        for char in s:
            if Counter(s[start:last+1]).most_common(1)[0][1] > 1:
                start += 1
            last += 1
        return last - start