class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        update=False
        for i in range(len(numbers)):
            other_num=self.binSearch(numbers, i+1, target-numbers[i])
            if  other_num !=-1 and i+1!=other_num+1:
                return [min(i+1, other_num+1),max(i+1, other_num+1)]
                
    def binSearch(self, numbers, start, target):
        left=0
        right=len(numbers)-1
        while left<=right:
            mid = (left+right)//2
            if numbers[mid]==target:
                return mid
            elif numbers[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1