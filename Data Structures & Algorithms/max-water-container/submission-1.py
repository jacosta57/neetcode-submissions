class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            length = right - left
            height = min(heights[left], heights[right])

            area = max(area, length * height)

            if heights[left] == height:
                left += 1
            else:
                right -= 1
        return area