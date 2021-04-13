class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        curr = 0
        
        for i in "(" + s + ")":
            if i.isdigit():
                curr = curr*10 + int(i)
            elif i == "(":
                stk += [0,'+']
                curr = 0
            elif i != " ":
                operator, prev = stk.pop(), stk.pop()
                curr = prev + (curr if operator == "+" else -curr)
                if i == ")":
                    continue
                stk += [curr, i]
                curr = 0
        return curr
                