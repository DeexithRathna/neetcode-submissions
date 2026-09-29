class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        left, right = 0, len(height)-1
        leftMax, rightMax = height[left], height[right]
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                max_water +=   leftMax  - height[left] 
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                max_water += rightMax - height[right]

        return max_water
        