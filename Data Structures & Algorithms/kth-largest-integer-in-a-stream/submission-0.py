class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.index=k
        self.nums = nums
        self.nums.sort()

    def add(self, val: int) -> int:
        for i in range(len(self.nums)):
            if self.nums[i] > val:
                self.nums.insert(i, val)
                return self.nums[-1*self.index]
        self.nums.append(val)
        return self.nums[-1*self.index]