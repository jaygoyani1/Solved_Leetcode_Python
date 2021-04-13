class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i == "(" or i == "{" or i =="[":
                stk.append(i)
            else:
                if not stk:
                    return False
                else:
                    x = stk.pop()
                    if i == ")":
                        if x != "(":
                            return False
                    elif i == "]":
                        if x != "[":
                            return False
                    else:
                        if x != "{":
                            return False
        if stk:
            return False
        return True
        