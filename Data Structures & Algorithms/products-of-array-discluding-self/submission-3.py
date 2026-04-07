class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1] * length
        postfix = [1] * length
        output = [0] * length

        for i in range(1, length):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        for i in range(length - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]

        for i in range(length):
            output[i] = postfix[i] * prefix[i]

        return output