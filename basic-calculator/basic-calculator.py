class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        i = 0
        sign = [1,1]
        
        while i<len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i <len(s) and s[i].isdigit():
                    i+=1
                total += sign.pop()*int(s[start:i])
                continue
            if c in "(+-":
                if c == "-":
                    sign.append(sign[-1]*(-1))
                else:
                    sign.append(sign[-1])
            elif c == ")":
                sign.pop()
            i+=1
        return total
#         stk = []
#         curr = 0
        
#         for i in "(" + s + ")":
#             if i.isdigit():
#                 curr = curr*10 + int(i)
#             elif i == "(":
#                 stk += [0,'+']
#                 curr = 0
#             elif i != " ":
#                 operator, prev = stk.pop(), stk.pop()
#                 curr = prev + (curr if operator == "+" else -curr)
#                 if i == ")":
#                     continue
#                 stk += [curr, i]
#                 curr = 0
#         return curr

                