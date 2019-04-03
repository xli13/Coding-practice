class Solution:
    def __init__(self):
        self.Stack1=[]
        self.Stack2=[]
    def push(self, node):
        # write code here
        self.Stack1.append(node)
    def pop(self):
        # return xx
        if self.Stack2==[]:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())
            return self.Stack2.pop()
        return self.Stack2.pop()
