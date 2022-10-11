class Solution:
    def __init__(self):
        self.expression = ""
        self.minValue = None
        self.num1 = ""
        self.num2 = ""
        self.seen = []
    
    def findMaxExpression(self,num1Start, num2End):
        if num1Start < 0 or num2End >= len(self.num2):
            return
        
        if self.seen[num1Start][num2End]:
            return
        self.seen[num1Start][num2End] = True
        value = int(self.num1[num1Start:]) + int(self.num2[:num2End + 1])
        if num1Start > 0:
            value *= int(self.num1[:num1Start])
        if num2End < len(self.num2) - 1:
            value *= int(self.num2[num2End +1:])

        if self.minValue == None or value < self.minValue:
            self.minValue = value
            expression = ""
            if num1Start > 0:
                expression += self.num1[:num1Start]
            expression += "(" + self.num1[num1Start:] + "+" + self.num2[:num2End+1] + ")"
            if num2End < len(self.num2) - 1:
                expression += self.num2[num2End+1:]
            self.expression = expression

        self.findMaxExpression(num1Start - 1, num2End)
        self.findMaxExpression(num1Start, num2End + 1)
    
    def minimizeResult(self, expression: str) -> str:
        self.num1, self.num2 = expression.split("+")
        self.seen = [[False for i in range(len(self.num2))] for j in range(len(self.num1))]
        
        self.findMaxExpression(len(self.num1) - 1, 0)
        
        return self.expression
            