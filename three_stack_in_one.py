class MultiStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.number_stacks = 3
        self.cust_size = [0] * (stack_size * self.number_stacks)
        self.sizes = [0] * self.number_stacks

    def is_full(self, stack_number):
        if self.sizes[stack_number] == self.stack_size:
            return True
        else:
            return False

    def is_empty(self, stack_number):
        if self.sizes[stack_number] == 0:
            return True
        else:
            return False

    def index_of_top(self, stack_number):
        print(stack_number,self.stack_size)
        offset = stack_number * self.stack_size
        print(offset,self.sizes[stack_number])
        return offset + self.sizes[stack_number] - 1

    def push(self, item, stack_number):
        if self.is_full(stack_number):
            return 'stack is full!'
        else:
            self.sizes[stack_number] +=1
            self.cust_size[self.index_of_top(stack_number)] = item

    def pop(self, stack_number):
        if self.is_empty(stack_number):
            return  'stack is empty!'
        else:
            value = self.cust_size[self.index_of_top(stack_number)]
            self.cust_size[self.index_of_top(stack_number)] = 0
            return  value

    def peek(self, stack_number):
        if self.is_empty(stack_number):
            return  'stack is empty!'
        else:
            value = self.cust_size[self.index_of_top(stack_number)]
            return  value

custome_stacks = MultiStacks(6)

print(custome_stacks.is_empty(0))
custome_stacks.push(1,0)





