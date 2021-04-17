class stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return 'the elemet has been added!'

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

custome_stack = stack()
print(custome_stack.is_empty())

custome_stack.push(1)
custome_stack.push(2)
custome_stack.push(3)


#custome_stack.pop()

print(custome_stack.peek())

print(custome_stack)


