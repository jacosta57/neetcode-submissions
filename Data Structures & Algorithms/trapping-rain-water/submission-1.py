class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)

        if length == 0:
            return 0

        left = [0] * length
        right = [0] * length
        water = 0

        left[0] = height[0]
        for i in range(1, length):
            left[i] = max(height[i], left[i - 1])

        right[length - 1] = height[length - 1]
        for i in range(length - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])
        
        for i in range(length):
            water += min(left[i], right[i]) - height[i]

        return water
