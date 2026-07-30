class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        while i<len(s):
            if (ord(s[i]) < 65 or ord(s[i]) > 90) and (ord(s[i]) < 97 or ord(s[i]) > 122) and (ord(s[i]) < 48 or ord(s[i]) > 57):
                if i==len(s)-1:
                    s=s[:i]
                else:
                    s=s[:i]+s[i+1:]
            else:
                i+=1
            print(s)
        s=s.lower()
        for i in range(len(s)):
            if s[i]!=s[-i-1]:
                return False
        return True