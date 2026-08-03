class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=-1
        digits[-1]+=1
        while digits[i]==10:
            digits[i]=0
            if i*-1<len(digits):
                digits[i-1]+=1
            else:
                digits.insert(0,1)
            i-=1
        return digits