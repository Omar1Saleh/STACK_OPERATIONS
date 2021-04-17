class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def is_empty(self):
        if self.linked_list.head is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def peek(self):
        if custom_stack.is_empty():
            return 'stack is empty!'
        else:
            return self.linked_list.head.value

    def pop(self):
        if custom_stack.is_empty():
            return 'stack is empty!'
        else:
            temp=self.linked_list.head
            self.linked_list.head=self.linked_list.head.next
            return temp.value

    def travers(self):
        if custom_stack.is_empty():
            return 'stack is empty!'
        values = []
        temp = self.linked_list.head
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        print('\n'.join(values))

    def delete(self):
        self.linked_list.head = None


custom_stack = Stack()
print(custom_stack.is_empty())
print(custom_stack.travers())


