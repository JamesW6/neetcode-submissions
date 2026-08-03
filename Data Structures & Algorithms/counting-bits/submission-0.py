class Solution:
    def countBits(self, n: int) -> List[int]:
        bits_array=[]
        for i in range(n+1):
            j=1
            bits=0
            while j<=i:
                if j&i:
                    bits+=1
                j=j<<1
            bits_array.append(bits)
        return bits_array