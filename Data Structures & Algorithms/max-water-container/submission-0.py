class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                height = j - i
                width = min(heights[i], heights[j])

                area = max(area, height * width)
        return area
        