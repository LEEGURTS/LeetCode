import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict = collections.defaultdict(list)
        for word in strs:
            dict["".join(sorted(word))].append(word)
        return dict.values()