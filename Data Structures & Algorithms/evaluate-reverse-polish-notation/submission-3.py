class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        operations = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operations:
                num1, num2 = stack.pop(), stack.pop()
                current = 0
                
                match token:
                    case "+":
                        current = num1 + num2
                    case "-":
                        current = num2 - num1
                    case "*":
                        current = num1 * num2
                    case "/":
                        current = int(num2 / num1)
                stack.append(current)
                print(current)
            else:    
                stack.append(int(token))
        return stack.pop()

