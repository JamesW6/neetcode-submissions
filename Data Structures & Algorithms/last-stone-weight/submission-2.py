class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            
            greatest=(0, -1)
            second_greatest=(0, -1)
            for i in range(len(stones)):
                if stones[i]>=greatest[0]:
                    second_greatest=greatest
                    greatest=(stones[i], i)
                elif stones[i]>=second_greatest[0]:
                    second_greatest=(stones[i],i)
            if greatest[0] == second_greatest[0]:
                stones.pop(greatest[1])
                stones.pop(second_greatest[1])
            else:
                stones[greatest[1]]=greatest[0]-second_greatest[0]
                stones.pop(second_greatest[1])
        if len(stones)>0:
            return stones[0]
        else:
            return 0
                