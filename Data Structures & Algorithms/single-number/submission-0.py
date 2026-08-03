class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        appearances=set()
        for num in nums:
            if num in appearances:
                appearances.remove(num)
            else:
                appearances.add(num)
        for num in appearances:
            return num