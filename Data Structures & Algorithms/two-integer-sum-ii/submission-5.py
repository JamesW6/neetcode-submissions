class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        found={}
        for i in range(len(numbers)):
            num=numbers[i]
            if target-num in found:
                return [found[target-num]+1,i+1]
            else:
                found[num]=i
        