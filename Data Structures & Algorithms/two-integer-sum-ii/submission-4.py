class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        found={}
        for i in range(1, len(numbers)+1):
            num=numbers[i-1]
            if target-num in found:
                return [found[target-num],i]
            else:
                found[num]=i
        