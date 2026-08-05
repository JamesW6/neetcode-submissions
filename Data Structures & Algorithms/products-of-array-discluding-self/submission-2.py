import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(len(products)):
                if j!=i:
                    products[j]*=nums[i]
        return products

