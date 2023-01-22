#Postfix to Infix

class Conversion:

    def __init__(self, capacity):

        self.top = -1
        self.capacity = capacity
        self.stack = []
        self.output = []
        self.precedence = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3}

    def is_empty(self):
        if self.top == -1:
            return True
        return False
    
    def peek(self):
        return self.stack[-1]
    
    def push(self, val):
        self.top +=1
        self.stack.append(val)
    
    def pop(self):
        if not self.is_empty():
            self.top-=1
            return self.stack.pop()
        return '$'
    
    def is_operand(self,op):
        return op.isalpha()
    
    def not_greater(self,i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a<=b else False
        except KeyError:
            return False
        
    def infix_to_postfix(self,exp):

        for i in exp:

            if self.is_operand(i):
                self.output.append(i)
            
            elif i == '(':
                self.push(i)
            
            elif i == ')':

                while (not self.is_empty()) and self.peek()!='(':
                    a=self.pop()
                    self.output.append(a)
                if (not self.is_empty()) and self.peek()!='(':
                    return -1
                else:
                    self.pop()

            else:
                while (not self.is_empty()) and self.not_greater(i):
                    self.output.append(self.pop())
                self.push(i)
            print(self.stack)
            print(self.output)
        while not self.is_empty():
            self.output.append(self.pop())

        print("".join(self.output))

exp = "a+b*c+d"
obj = Conversion(len(exp))
obj.infix_to_postfix(exp)

