import collections
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        result = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
        count = collections.Counter(result)
        return count.most_common(1)[0][0]
