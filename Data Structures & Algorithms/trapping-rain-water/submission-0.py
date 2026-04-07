class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        length = len(height)
        water = 0

        for i in range(length):
            left = height[i]
            right = height[i]

            for j in range(i):
                left = max(left, height[j])
            for j in range(i + 1, length):
                right = max(right, height[j])
            
            water += min(left, right) - height[i]
        return water
            
