class Solution:
    def climbStairs(self, n: int) -> int:
        first=1
        second=2
        total=0
        for i in range(n-2):
            total=first+second
            first=second
            second=total
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return total