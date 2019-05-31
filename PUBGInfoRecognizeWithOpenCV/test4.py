from multiprocessing import Queue

q=Queue()

q.put('aaaa')
q.get()

print(q.empty())