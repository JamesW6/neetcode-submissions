class Solution:
    def rob(self, nums: List[int]) -> int:
        best = 0
        robnext = 0
        for num in nums:
            if robnext+num>best:
                temp = best
                best = robnext + num
                robnext = temp
            else:
                robnext = best
        return best


                