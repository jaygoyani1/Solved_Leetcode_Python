class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {"(": ")", "{": "}", "[": "]"}
        
        stack = []
        
        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                if mapping[stack.pop()] != char:
                    return False
        return len(stack) == 0
            