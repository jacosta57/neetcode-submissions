class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                current = stack.pop()

                match s[i]:
                    case "}":
                        if current != "{":
                            return False
                    case "]":
                        if current != "[":
                            return False
                    case ")":
                        if current != "(":
                            return False
        return len(stack) == 0