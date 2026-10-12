class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = 0

        while left < right:
            width = right - left
            water = min(height[left], height[right]) * width

            maxWater = max(maxWater, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater