class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * length
        postfix = [0] * length
        output = [0] * length

        for i in range(length):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i - 1]

        for i in range(length):
            j = length - 1 - i
            if j == length - 1:
                postfix[j] = nums[j]
            else:
                postfix[j] = nums[j] * postfix[j + 1]


        for i in range(length):
            if i == 0:
                output[i] = postfix[i + 1]
            elif i == length - 1:
                output[i] = prefix[i - 1]
            else:
                output[i] = postfix[i + 1] * prefix[i - 1]

        return output