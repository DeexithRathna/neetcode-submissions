class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        mid = ( low + high ) // 2
        while ( low < high and mid != low and mid != high):
            # print(low, mid, high)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid
            else:
                high = mid
            mid = ( low + high ) // 2
        if target == nums[mid]:
            return mid
        return -1

        