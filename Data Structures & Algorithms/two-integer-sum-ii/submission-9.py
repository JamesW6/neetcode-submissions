class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        update=False
        for i in range(len(numbers)):
            num=numbers[i]
            if numbers[i]==target-num:
                numbers[i]-=1
                update=True
            other_num=self.binSearch(numbers, target-num)
            if  other_num !=-1 and i+1!=other_num+1:
                return [i+1, other_num+1]
            if update:
                numbers[i]+=1
                update=False
                
    def binSearch(self, numbers, target):
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