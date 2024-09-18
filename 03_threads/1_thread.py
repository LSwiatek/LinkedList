import threading
import random
import time


ten_mln_list = []
for n in range(0, 10000000):
    number = random.randint(0, 10000000)
    ten_mln_list.append(number)

# print(ten_mln_list)


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


class SortingProcess:

    def __init__(self, list_to_sort):
        self.list_to_sort = list_to_sort

    def sort(self):
        self.sorted = merge_sort(self.list_to_sort)

    def get_sorted(self):
        if self.sorted is None:
            self.sort()
        return self.sorted


sorting_process = SortingProcess(ten_mln_list)


new_thread = threading.Thread(target=lambda:sorting_process.sort())

start_time = time.clock_gettime_ns(time.CLOCK_REALTIME)
new_thread.start()
new_thread.join()
finish_time = time.clock_gettime_ns(time.CLOCK_REALTIME)
print(sorting_process.get_sorted())

print((finish_time - start_time) / 1e9)


