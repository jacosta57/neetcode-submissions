class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()
        for num in nums:
            if num not in seen:
                seen[num] = 0
            seen[num] += 1
        sorted_items = sorted(seen, key=lambda num: seen[num], reverse=True)
        return sorted_items[:k]