'''
we create a stack using list, with fixed size, if the size of this stack is exceeded
we create a nother stack with same size, using nested lists. 
'''
class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    def push(self, item):
        # check if the stacksize not exceeded then we add element to current nested list
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            # if stack size is exceeded or there is no list at all we create a new nested list
            self.stacks.append([item])

    def pop(self):
        # checking if there are any empty nested list, and removing before popping any elements
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None

customStack = PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.pop_at(1))
