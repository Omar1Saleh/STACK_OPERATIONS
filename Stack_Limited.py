class stack:
    def __init__(self, max_size):
        self.list = []
        self.max_size = max_size

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def is_full(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    def push(self, value):
        if self.is_full():
            return 'the stack is full!'
        else:
            self.list.append(value)
            return 'element inserted!'

    def pop(self):
        if self.is_empty():
            return 'there are no elements!'
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return 'there are no elements!'
        else:
            return self.list[-1]

    def delete(self):
        self.list = None

custome_stack = stack(4)
print(custome_stack.is_empty())
print(custome_stack.is_full())
custome_stack.push(1)
custome_stack.push(2)
custome_stack.push(3)
custome_stack.push(4)
print(custome_stack.peek())


