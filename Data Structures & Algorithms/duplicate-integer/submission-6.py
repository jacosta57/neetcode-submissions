class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in range(len(nums)):
            current_num = nums[i]
            if current_num in seen:
                return True
            seen.add(current_num)
        return False