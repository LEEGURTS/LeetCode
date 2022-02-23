import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, start, end = 0, 0, 0
        need = collections.Counter(t)
        missed = len(t)
        for right, char in enumerate(s, 1):
            missed -= need[char] > 0
            need[char] -= 1

            if missed == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]]+=1
                    left+=1

                if not end or right - left <= end -start:
                    start, end = left,right
                    need[s[left]]+=1
                    missed +=1
                    left+=1
        return s[start:end]



