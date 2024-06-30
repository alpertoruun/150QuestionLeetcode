class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        maximumArea=0
        current_sum=0
        while left < right:
            current_sum = min(height[left],height[right]) * (right-left)
            if current_sum > maximumArea:
                maximumArea= current_sum
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        
        return maximumArea
        
        