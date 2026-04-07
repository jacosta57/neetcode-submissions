class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    products[i] *= nums[j]
        return products