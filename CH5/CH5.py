# 1. 解釋 stack 跟 queue 是什麼? 他們的差別是?

# A: stack(堆疊)-先進後出(FILO)、queue(佇列)-先進先出(FIFO)

stack = []
for x in range(1,6):
	stack.append(x)   #入
	print('push', x, end=' ')
	print(stack)

print('Now stack is', stack)

while len(stack)>0:
	print('pop', stack.pop(), end=' ') #出
	print(stack)


from collections import deque
queue = deque()
for x in range(1,6):
	queue.append(x)   # 入
	print('push', x, end=' ')
	print(list(queue))

print('Now queue is', list(queue))

while len(queue)>0:
	print('pop', queue.popleft(), end=' ')  # 出
	print(list(queue))

# 2. 實作一個queue class kqueue, 並提供 kqueue.push(), kqueue.pop(), kqueue.size(), kqueue.front(), kqueue.back() 的功能

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

    
# 3. 實作一個stack class kstack, 並提供 kstack.push(), kstack.pop(), kstack.size(), kstack.top() 的功能

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

# 4. 將上面兩個分別打包成 ktool 的 module

from ktool import kqueue,kstack


# 5. 分別使用 ktool 裡的 kqueue 及 kstack 對 [2,3,1,9,22,31,8,7,45,9] 由小到大做排序

x = [2,3,1,9,22,31,8,7,45,9]
queue = kqueue.kqueue()
queue_temp = kqueue.kqueue()

for element in x:
	if queue.size() == 0 or element >= queue.back():
		queue.push(element)
	else:
		while queue.size() != 0 and element >= queue.front():
			queue_temp.push(queue.pop())
		else:
			queue_temp.push(element)
			while queue.size() != 0:
				queue_temp.push(queue.pop())
			while queue_temp.size() != 0:
				queue.push(queue_temp.pop())

print("kqueue:", queue.queue)


x = [2,3,1,9,22,31,8,7,45,9]
stack = kstack.kstack()
stack_temp = kstack.kstack()

for element in x:
	if stack.size() == 0 or element >= stack.top():
		stack.push(element)
	else:
		while stack.size() != 0 and element < stack.top():
			stack_temp.push(stack.pop())
		else:
			stack.push(element)
			while stack_temp.size() != 0:
				stack.push(stack_temp.pop())

print("kstack:", stack.stack)