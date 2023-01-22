#Postfix Evaluation

class Evaluate:
    
    def __init__(self,capacity):
        self.top = -1
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return True if self.top==-1 else False
    
    def peek(self):
        return self.stack[-1]
    
    def push(self,val):
        self.top+=1
        self.stack.append(val)

    def pop(self):
        if not self.is_empty():
            self.top-=1
            return self.stack.pop()
        else:
            return '$'
    
    def postfix_eval(self, exp):

        for i in exp:
            if i.isdigit():
                self.push(i)
            
            else:
                val1 = self.pop()
                val2 = self.pop()
                if i == '/':
                    i='//'
                self.push(str(eval(val2 + i + val1)))
    
        return int(self.pop())

exp = "08/"

obj = Evaluate(len(exp))
print(obj.postfix_eval(exp))
