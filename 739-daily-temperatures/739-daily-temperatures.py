class Solution:
    def dailyTemperatures(self, tem: List[int]) -> List[int]:
        result = [0] * len(tem)
        stack = []
        for i,cur in enumerate(tem):
            while stack and cur > tem[stack[-1]]:
                last = stack.pop()
                result[last] = i-last
            stack.append(i)
            
        return result