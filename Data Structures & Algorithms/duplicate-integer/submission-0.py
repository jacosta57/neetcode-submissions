class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Two ways to solve this, A Two pointer Approach or a 1 pass Hashmap
        # We will do a 1 Pass Hashmap

        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else:
                hashmap[nums[i]] = i
        
        return False
        