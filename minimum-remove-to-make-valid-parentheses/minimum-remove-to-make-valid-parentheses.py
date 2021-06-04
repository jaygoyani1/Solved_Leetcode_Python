class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        remove = set()
        stk = []
        for i,char in enumerate(s):
            if char not in "()":
                continue
            if char == "(":
                stk.append(i)
            elif not stk:
                remove.add(i)
            else:
                stk.pop()
        res = []
        for i in stk:
            remove.add(i)
        
        for i,char in enumerate(s):
            if i not in remove:
                res.append(char)
        return "".join(res)
            
        