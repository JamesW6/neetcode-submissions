class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        input: array of heights of bars that can hold water
        output: the amount of water that can be held in best case
        '''
        best=0
        left=0
        right=len(heights)-1
        while(left<right):
            if heights[left]>heights[right]:
                best = max( heights[right] * (right-left), best)
                right-=1
            else:
                best = max( heights[left] * (right-left), best)
                left+=1
        return best