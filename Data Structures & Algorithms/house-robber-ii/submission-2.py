class Solution:
    def rob(self, nums: List[int]) -> int:
        robNext = 0
        best = 0
        if len(nums)==1:
            return nums[0]
        for i in range(1, len(nums)):
            if robNext+nums[i]>best:
                temp = best
                best = robNext + nums[i]
                robNext = temp
            else:
                robNext = best
        robNext2 = 0
        best2 = 0
        for i in range(1, len(nums)):
            if robNext2+nums[-i-1]>best2:
                temp=best2
                best2 = robNext2+nums[-i-1]
                robNext2 = temp
            else:
                robNext2 = best2
        return max(best, best2)