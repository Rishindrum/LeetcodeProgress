class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operations = {"+": lambda x,y: x+y,
                      "-": lambda x,y: x-y, 
                      "*": lambda x,y: x*y, 
                      "/": lambda x,y: int(x/y)}

        for token in tokens:
            if token in operations:
                secondNum = numbers.pop()
                firstNum = numbers.pop()
                numbers.append(operations[token](firstNum, secondNum))                
            else:
                numbers.append(int(token))

        return numbers[0]
