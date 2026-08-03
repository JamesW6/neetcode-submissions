class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers=set()
        while True:
            nums=[]
            for i in range(int(math.log(n,10))+1):
                nums.append(n%10)
                n=int(n/10)
            for num in nums:
                n+=num*num
            if n==1:
                return True
            elif n in seen_numbers:
                return False
            seen_numbers.add(n)