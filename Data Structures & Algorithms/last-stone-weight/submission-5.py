class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            greatest = max(stones[0], stones[1])
            second_greatest=min(stones[0], stones[1])
            for i in range(2, len(stones)):
                if stones[i]>=greatest:
                    second_greatest=greatest
                    greatest=stones[i]
                elif stones[i]>=second_greatest:
                    second_greatest=stones[i]
            if greatest == second_greatest:
                stones.remove(greatest)
                stones.remove(second_greatest)
            else:
                stones.remove(greatest)
                stones.remove(second_greatest)
                stones.append(greatest-second_greatest)
        if len(stones)>0:
            return stones[0]
        else:
            return 0
                