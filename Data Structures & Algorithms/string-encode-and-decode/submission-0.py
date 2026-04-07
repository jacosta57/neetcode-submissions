class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = list()
        for i in range(len(strs)):
            count = str(len(strs[i]))
            encoded_strs.append(count + "#" + strs[i])
        return "".join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        decoded_strs = list()
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            i = int(s[i:j]) + j + 1
            decoded_strs.append(s[j + 1:i])
        return decoded_strs


