class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        longest = 0
        left = 0

        for right in range(len(s)):
            while s[right] in characters:
                characters.remove(s[left])
                left += 1
            characters.add(s[right])
            longest = max(longest, right - left + 1)
        return longest