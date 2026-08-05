class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        found_zero=False
        arr=[]
        for num in nums:
            if num:
                product*=num
            else:
                if found_zero:
                    return [0]*len(nums)
                found_zero=True
        if found_zero:
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
