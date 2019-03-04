class kstack:

    def __init__(self):
        self.stack = []

    def push(self, item):
	    return self.stack.append(item)

    def pop(self):
	    return self.stack.pop()

    def size(self):
	    return len(self.stack)

    def top(self):
        return self.stack[0]