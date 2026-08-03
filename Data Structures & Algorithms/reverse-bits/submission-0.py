class Solution:
    def reverseBits(self, n: int) -> int:
        new_n=0
        i=0
        while n:
            new_n=new_n | (n&1)<<(31-i)
            i+=1
            n=n>>1
        return new_n