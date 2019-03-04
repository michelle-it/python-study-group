class kqueue:

    def _init(self):
        self.queue = []

    def push(self, item):
	    return self.queue.append(item)

    def pop(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def front(self):
        return self.queue[0]

    def back(self):
        return self.queue[-1]
