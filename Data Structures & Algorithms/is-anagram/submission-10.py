class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        str1_hashmap = defaultdict()
        str2_hashmap = defaultdict()

        for i in range(len(s)):
            str1_hashmap[s[i]] = 1 + str1_hashmap.get(s[i], 0)
            str2_hashmap[t[i]] = 1 + str2_hashmap.get(t[i], 0)
        return str1_hashmap == str2_hashmap