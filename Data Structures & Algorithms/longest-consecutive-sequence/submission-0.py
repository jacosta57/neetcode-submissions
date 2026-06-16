class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = set(nums)
        sequence = 0

        for num in sorted_nums: 
            if num - 1 not in sorted_nums:
                current_num = num
                current_sequence = 1
                while current_num + 1 in sorted_nums:
                    current_num += 1
                    current_sequence += 1
                sequence = max(current_sequence, sequence)

        return sequence