class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def helper(i):
            
            # Base case
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            # Choice
            subset.append(nums[i])
            helper(i+1)

            # Backtrack
            subset.pop()
            helper(i+1)
        
        helper(0)
        return result
            



        