class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        onesCount = 0
        maxOnes = 0
        for i in nums:
            if i == 1:
                onesCount = onesCount + 1
                if onesCount > maxOnes:
                    maxOnes = onesCount
            else:
                onesCount = 0
        return maxOnes
        