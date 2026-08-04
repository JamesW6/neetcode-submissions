"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        self.merge_sort(intervals,0,len(intervals)-1)
        for i in range(len(intervals)-1):
            if intervals[i].end>intervals[i+1].start:
                return False
        return True
    def merge_sort(self, intervals:List[Interval],start:int,end:int) -> List[Interval]:
        if start<end:
            mid=(start+end)//2
            self.merge_sort(intervals,start,mid)
            self.merge_sort(intervals,mid+1,end)
            self.merge(intervals,start,mid,end)
    def merge(self, intervals:List[Interval], start:int,mid:int,end:int):
        n1=mid-start+1
        n2=end-mid
        left_array=[0]*n1
        right_array=[0]*n2
        for i in range(n1):
            left_array[i]=intervals[start+i]
        for i in range(n2):
            right_array[i]=intervals[mid+i+1]
        i=j=0
        k=start
        while i<n1 and j<n2:
            if left_array[i].start<right_array[j].start:
                intervals[k]=left_array[i]
                i+=1
            else:
                intervals[k]=right_array[j]
                j+=1
            k+=1
        while i<n1:
            intervals[k]=left_array[i]
            i+=1
            k+=1
        while j<n2:
            intervals[k]=right_array[j]
            j+=1
            k+=1
