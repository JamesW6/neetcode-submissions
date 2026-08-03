class Solution:
    def reverseBits(self, n: int) -> int:
        new_n=0
        for i in range(31,-1, -1):
            new_n=new_n | (n&1)<<(i)
            n=n>>1
        return new_n