class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = dict()

        for num in nums:
            if num not in groups:
                groups[num] = 0
            groups[num] += 1
        
        sorted_groups = sorted(groups, key=lambda num: groups[num], reverse=True)
        return sorted_groups[:k]