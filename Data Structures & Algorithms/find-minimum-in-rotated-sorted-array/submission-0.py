class Solution:
    def findMin(self, nums: List[int]) -> int:
        lowest = nums[0]

        for num in nums:
            if num < lowest:
                lowest = num

        return lowest