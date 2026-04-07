class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = defaultdict(list)
        length = len(nums)

        for i in range(length):
           for j in range(i + 1, length):
              for k in range(j + 1, length):
                 summ = nums[i] + nums[j] + nums[k]
                 triplet = sorted([nums[i], nums[j], nums[k]])
                 if triplet not in triplets[summ]:
                     triplets[summ].append(triplet)

        return triplets[0]