class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N=len(nums)
        suffix_prod=[0]*N
        for i in range(N-1,-1,-1):
            if(i==N-1):
                suffix_prod[i]=1
            else:
                suffix_prod[i]=suffix_prod[i+1]*nums[i+1]
        prefix_prod=[0]*N
        for i in range(N):
            if i==0:
                prefix_prod[i]=1
            else:
                prefix_prod[i]=prefix_prod[i-1]*nums[i-1]
        for i in range(N):
            prefix_prod[i]*=suffix_prod[i]

        return prefix_prod

