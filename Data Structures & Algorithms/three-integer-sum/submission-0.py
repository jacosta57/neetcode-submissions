class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    summ = nums[i] + nums[j] + nums[k]
                    if summ == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        triplets.add(triplet)
        return [list(triplet) for triplet in triplets]