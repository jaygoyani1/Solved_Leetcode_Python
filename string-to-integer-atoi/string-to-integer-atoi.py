class Solution:
    def myAtoi(self, s: str) -> int:

        a = list(s.strip(" "))
        if len(a) == 0:
            return 0
        flag = True
        
        if a[0] == "-":
            flag = False
        i = 0
        if a[0] == "-" or a[0] =="+":
            i = 1
        st= ""
        while i < len(a) and a[i].isdigit():
            st += a[i]
            i+=1
        if st == "":
            return 0
        num = int(st)
        if flag and num > (2**31-1):
            return 2**31 - 1
        if not flag and num > 2**31:
            return -2**31
        if not flag:
            num = -num
        return num