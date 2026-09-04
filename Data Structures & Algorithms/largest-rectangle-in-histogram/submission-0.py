class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        biggest = 0
        stack = list()

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                biggest = max(biggest, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            biggest = max(biggest, h * (len(heights) - i))
        return biggest