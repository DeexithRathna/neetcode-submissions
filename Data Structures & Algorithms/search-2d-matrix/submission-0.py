class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target <= row[-1] :
                # perform Binary Search
                if self.binarySearch(row, target):
                    return True
        return False
    
    def binarySearch(self, arr, target):
        l,r = 0, len(arr)
        while l <= r:
            m = (l + r ) // 2
            if arr[m] < target:
                l = m + 1
            elif arr[m] > target:
                r = m - 1
            else:
                return True
        return False
        