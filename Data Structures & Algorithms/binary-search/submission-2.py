class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            middle = left + ((right - left) // 2)
            current_num = nums[middle]
            if current_num == target:
                return middle
            elif current_num < target:
                left = middle + 1
            elif current_num > target:
                right = middle
        return -1