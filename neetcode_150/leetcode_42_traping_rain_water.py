class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        # Initialize arrays to store max height from left and right
        left_max = [0] * n
        right_max = [0] * n
        
        # Fill left_max: max height seen so far from the left
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
            
        # Fill right_max: max height seen so far from the right
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
            
        # Calculate trapped water
        total_water = 0
        for i in range(n):
            # Water level is limited by the shorter of the two walls
            water_level = min(left_max[i], right_max[i])
            # Add water trapped above the current bar
            total_water += water_level - height[i]
            
        return total_water   