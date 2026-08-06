class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        found={}
        for i in range(len(numbers)):
            num=numbers[i]
            if target-num in found:
                return [found[target-num],i+1]
            else:
                found[num]=i+1
        