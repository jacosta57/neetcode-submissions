class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        concatenation = [0] * (2 * size)

        for i, num in enumerate(nums):
            concatenation[i] = concatenation[i + size] = num
        
        return concatenation
        