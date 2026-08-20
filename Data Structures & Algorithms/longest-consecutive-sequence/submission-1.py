class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        max_count = 1
        if nums:
            previous = nums[0]
            print(nums)
            for i in range(1, len(nums)):
                if nums[i] - previous == 1:
                    count = count + 1
                elif nums[i] == previous:
                    continue
                else:
                    count = 1
                max_count = max(count, max_count)
                previous = nums[i]
            return max_count
        else:
            return 0
        