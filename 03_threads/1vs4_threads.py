import threading
import random
import time


ten_mln_list = []
for n in range(0,100):
    number = random.randint(0, 10000000)
    ten_mln_list.append(number)

print(ten_mln_list)


def merge_sort(list):
    if len(list) == 1:
        return list

    n = len(list)//2
    right = list[n:]
    left = list[:n]
    sorted_right = merge_sort(right)
    sorted_left = merge_sort(left)
    i = 0
    j = 0
    result = []
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] <= sorted_right[j]:
            result.append(sorted_left[i])
            i += 1
        else:
            result.append(sorted_right[j])
            j += 1
    if i < len(sorted_left):
        result += sorted_left[i:]
    if j < len(sorted_right):
        result += sorted_right[j:]
    return result


class ThreadWithReturnValue(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return


single_thread = ThreadWithReturnValue(target=merge_sort, args=[ten_mln_list])
single_thread.start()
print(single_thread.join())


print(time.thread_time())


#using 4 threads:

threads = []

for i in range(4):
    thread_name = f"Thread-{i+1}"
    thread = ThreadWithReturnValue(target=merge_sort, args=[ten_mln_list])
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    print(thread.join())

print(time.thread_time())


