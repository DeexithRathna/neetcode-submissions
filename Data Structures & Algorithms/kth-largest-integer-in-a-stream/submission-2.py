class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k
        
    def binarySearch(self, val):
        if not self.nums:
            return 0
        else:
            low = 0
            high = len(self.nums) - 1
            middle = ( low + high ) // 2
            while low < high and middle != low and middle != high:
                if self.nums[middle] <= val:
                    low = middle
                else:
                    high = middle
                middle = ( low + high ) // 2
            return middle

    def add(self, val: int) -> int:
        if self.nums:
            if val >= self.nums[-1] :
                self.nums.append(val)
            elif val <= self.nums[0]:
                self.nums = [val] + self.nums
            else:
                index = self.binarySearch(val)
                self.nums.insert(index+1, val)
            return self.nums[-self.k]
        else:
            self.nums = []
            self.nums.append(val)
            return val

        # Ignoring length check as it is explictly mentioned that atleast k are present

        
