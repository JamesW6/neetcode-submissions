class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        threshold=0
        most_frequent=set()
        for num in nums:
            if num in frequency:
                frequency[num]+=1
            else:
                frequency[num]=1
            if frequency[num]>=threshold and num not in most_frequent:
                most_frequent.add(num)
            if len(most_frequent)>k:
                threshold=frequency[num]+1
                i=0
                new_most_frequent=most_frequent.copy()
                for item in most_frequent:
                    if frequency[item]<threshold:
                        new_most_frequent.remove(item)
                most_frequent=new_most_frequent
        return list(most_frequent)