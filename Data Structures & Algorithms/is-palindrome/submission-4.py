class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        while i<len(s):
            if not s[i].isalnum():
                if i==len(s)-1:
                    s=s[:i]
                else:
                    s=s[:i]+s[i+1:]
            else:
                i+=1
        s=s.lower()
        for i in range(len(s)):
            if s[i]!=s[-i-1]:
                return False
        return True