class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        found={}
        for i in range(len(numbers)):
            if target-numbers[i] in found:
                return [found[target-numbers[i]],i+1]
            else:
                found[numbers[i]]=i+1
        