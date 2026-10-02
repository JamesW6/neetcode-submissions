class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        input: list of numbers 
        output: list of triplets that sum to zero

        constraints:
        it is possible for there to be no triplets
        minimum of 3 numbers in nums
        values in nums can be negative
        i!=j!=k

        approaches:
        iterate through array, keep track of k in hashmap, then two pointers 
        [-1,0,1,2,-1,-4]
        brute force: 
        3 nested loop, sum all values, iterate
        
        pseudocode:
        iterate through loop, nested with pointers i and j
        see if j is in map, if it is, and i!=j!=k, add them
        sum i and j, and then multiply by -1, and add to the map if not in, 
        '''
        need={}
        valids=[]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if -1*(nums[i]+nums[j]) in need:
                    val=need[-1*(nums[i]+nums[j])]
                    if i!=j and i!=val and val!=j:
                        to_add=[nums[i], nums[j], nums[val]]
                        to_add.sort()
                        if to_add not in valids:
                            valids.append(to_add)
            if nums[i] not in need:
                need[nums[i]]=i
        return valids