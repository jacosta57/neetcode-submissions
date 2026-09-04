class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        leftIdx = 0
        longest = 0

        for rightIdx in range(len(s)):
            while s[rightIdx] in characters:
                characters.remove(s[leftIdx])
                leftIdx += 1

            characters.add(s[rightIdx])
            longest = max(longest, 1 + rightIdx - leftIdx)
        return longest