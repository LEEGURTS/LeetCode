import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = max_len = 0
        count = collections.Counter()
        for i,string in enumerate(s):
            count[string] += 1
            common = count.most_common(1)[0][1]

            if i + 1 - left - common > k:
                count[s[left]] -= 1
                left += 1
                
        return len(s)-left
