class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared={}
        for num in nums:
            if num in appeared:
                return True
            else:
                appeared[num]=1
        return False