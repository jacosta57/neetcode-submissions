class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = dict()
        left = 0
        longest = 0
        maxFrequency = 0

        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right], 0) + 1
            maxFrequency = max(maxFrequency, frequency[s[right]])

            while (right - left + 1) - maxFrequency > k:
                frequency[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest