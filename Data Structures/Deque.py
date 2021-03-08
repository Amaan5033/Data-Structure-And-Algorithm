


# How to use collections.deque as a FIFO queue


# from collections import deque

# customQueue=deque(maxlen=3)

# print(customQueue)

# customQueue.append(1)
# customQueue.append(2)
# customQueue.append(3)
# customQueue.append(4)


# customQueue.popleft()

# customQueue.clear()
# print(customQueue)



# How to use Queue module

# import queue as q

# customQueue=q.Queue(maxsize=3)
# print(customQueue.qsize())
# print(customQueue.empty())
# customQueue.put(1)
# customQueue.put(2)
# customQueue.put(3)
# print(customQueue.empty())
# print(customQueue.full())
# print(customQueue.get())
# print(customQueue.qsize())



# how to use multiprocessing module



from multiprocessing import Queue

customQueue=Queue(maxsize=3)

# We cannot use join method and taskDOne











