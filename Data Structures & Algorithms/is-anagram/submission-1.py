class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersS={}
        lettersT={}
        for letter in s:
            if letter in lettersS:
                lettersS[letter]+=1
            else: 
                lettersS[letter]=1
        for letter in t:
            if letter in lettersT:
                lettersT[letter]+=1
            else: 
                lettersT[letter]=1
        for key in lettersS:
            if key not in lettersT:
                return False
            if lettersS[key]!=lettersT[key]:
                return False
        for key in lettersT:
            if key not in lettersS:
                return False
            if lettersS[key]!=lettersT[key]:
                return False
        return True