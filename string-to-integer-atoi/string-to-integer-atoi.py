class Solution:
    def myAtoi(self, s: str) -> int:
        
        
        i = 0
        negative = False
        number = 0
            
        while i<len(s) and s[i] == " ":
            i+=1

        if i<len(s):
            if s[i] == "-":
                negative = True
                i+=1
            elif s[i] == "+":
                i+=1

        while i<len(s):
            if not s[i].isdigit():
                break
            number =number*10 + int(s[i])
            i+=1
        
        number = -number if negative else number
        
        if number > (2**31-1):
            return 2**31-1
        if number < (-2**31):
            return -2**31
        return number
                


                
            