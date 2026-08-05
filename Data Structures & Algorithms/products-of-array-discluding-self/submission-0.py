class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        found_zero=False
        two_zeros=False
        arr=[]
        for num in nums:
            if num:
                product*=num
            else:
                if found_zero:
                    two_zeros=True
                found_zero=True
        if two_zeros:
            return [0]*len(nums)
        elif found_zero:
            for num in nums:
                if num:
                    arr.append(0)
                else:
                    arr.append(product)
        else:
            for num in nums:
                if num:
                    arr.append(product//num)
                else:
                    arr.append
        return arr
