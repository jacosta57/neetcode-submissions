class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        currentCount = 0

        for num in nums:
            if num == 0:
                maxCount = max(maxCount, currentCount)
                currentCount = 0
            if num == 1:
                currentCount += 1
        return max(maxCount, currentCount)