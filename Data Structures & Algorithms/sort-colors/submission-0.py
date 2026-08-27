class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0,0,0]
        for i in range(len(nums)):
            freq[nums[i]] += 1
        
        index = 0
        for color, i in enumerate(freq):
            for j in range(i):
                nums[index] = color
                index += 1
        return nums

        