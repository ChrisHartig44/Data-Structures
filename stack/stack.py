class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Part 2: linked list implementation
class Stack:
    def __init__(self):
        self.first = None
        self.count = 0

    def __len__(self):
        return self.count

    def push(self, value):
        if self.first is None:
            self.first = Node(value)
        else:
            node = Node(value, next=self.first)
            self.first = node
        self.count += 1

    def pop(self):
        if self.first is None:
            return None
        elif self.first.next is None:
            node = self.first
            self.first = None
            self.count -= 1
            return node.value
        else:
            node = self.first
            self.first = self.first.next
            self.count -= 1
            return node.value


# Part 1: array implementation
class ListStack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if self.storage:
            return self.storage.pop()
        else:
            return None