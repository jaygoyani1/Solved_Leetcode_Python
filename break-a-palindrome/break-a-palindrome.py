class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        n = len(palindrome)//2
        flag = True
        for i in range(n):
            if palindrome[i] != "a":
                palindrome = palindrome[:i]+"a"+palindrome[i+1:]
                return palindrome
        
        for i in range(len(palindrome)-1,n-1,-1):

            if palindrome[i] == "a":
                palindrome = palindrome[:i]+"b"+palindrome[i+1:]
                return palindrome
        return ""        