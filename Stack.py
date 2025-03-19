class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1


    def is_empty(self):
        if self.top == -1:
            return 1
        else:
            return -1

    def push(self, element):
            self.stack.append(element)
            self.top = self.top + 1
            print(element)
            print('Element added !!!')
            print(self.stack)

    def pop(self):
        if self.is_empty() == 1:
            print('Stack Underflow')

        else:
            self.stack.pop()
            self.top = self.top - 1
            print('Last element is Removed...!!!')
            print(self.stack)

    def peek(self):
        print('Element on the top ')
        print(self.stack[-1])
s = Stack()

s.push(22)
s.push(12)
s.push(23)
s.push(25)
s.push(24)
s.push(299)
s.pop()