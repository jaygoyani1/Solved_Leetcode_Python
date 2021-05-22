class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def backtrack(curr_list,op,cl):
            if len(curr_list) == n*2:
                res.append("".join(curr_list))
                return
            if op<n:
                curr_list.append("(")
                backtrack(curr_list,op+1,cl)
                curr_list.pop()
            if cl<op:
                curr_list.append(")")
                backtrack(curr_list, op, cl+1)
                curr_list.pop()
        backtrack([],0,0)
        return res
        