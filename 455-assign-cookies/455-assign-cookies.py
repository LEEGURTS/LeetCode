class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        count = 0
        s.sort()
        g.sort()
        while s and g:
            temp = s.pop()
            while g:
                temp2 = g.pop()
                if temp2 <= temp:
                    break
            if temp >= temp2:
                count+=1
        return count