class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for text in s:
            if text not in table:
                stack.append(text)
            elif not stack or table[text] != stack.pop():
                return False
        return len(stack) == 0
