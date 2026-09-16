class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            middle = left + (right - left) // 2
            current = nums[middle]

            if current == target:
                return middle
            elif current < target:
                left = middle + 1
            elif current > target:
                right = middle

        return -1