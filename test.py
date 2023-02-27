import queue

q_ax = queue.Queue(maxsize=5)
q_ax.put(float(1.12))
q_ax.put(float(1.12))
q_ax.put(float(1.12))
q_ax.put(float(1.12))
q_ax.put(float(1.12))




print(q_ax.full())
print(list(q_ax.queue))
print(range(0, len(list(q_ax.queue))))
print(q_ax.full())
