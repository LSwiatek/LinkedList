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
    return merge(sorted_left, sorted_right)


def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]
    return result


class SortingProcess:

    def __init__(self, list_to_sort, thread_number):
        print(thread_number)
        self.list_to_sort = list_to_sort
        self.thread_number = thread_number

    def sort(self):
        print(f"started sorting thread {self.thread_number}")
        self.sorted = merge_sort(self.list_to_sort)
        print(f"finished sorting thread {self.thread_number}")

    def get_sorted(self):
        print(f"started get sorted thread {self.thread_number}")
        if self.sorted is None:
            self.sort()
        return self.sorted



A = ten_mln_list[:len(ten_mln_list) // 4]
B = ten_mln_list[len(ten_mln_list) // 4: len(ten_mln_list) // 2]
C = ten_mln_list[len(ten_mln_list) // 2 : len(ten_mln_list) * 3 // 4]
D = ten_mln_list[len(ten_mln_list) * 3 // 4:]

divided_list = [A] + [B] + [C] + [D]

# print(divided_list)

threads = []

def print_sth(name):
    while True:
        print(name)


sorting_processes = []

n = 0
for elem in divided_list:
    thread_name = f"Thread-{divided_list.index(elem)+1}"
    sorting_process = SortingProcess(elem, thread_name)
    n = n + 1
    sorting_processes.append(sorting_process)
    t = threading.Thread(target=sorting_process.sort)
    threads.append(t)

start_time = time.clock_gettime_ns(time.CLOCK_REALTIME)

for thread in threads:

    thread.start()

for thread in threads:
    thread.join()

merged_A_B, merged_C_D = merge(sorting_processes[0].get_sorted(), sorting_processes[1].get_sorted()), merge(sorting_processes[2].get_sorted(), sorting_processes[3].get_sorted())
merged_list = merge(merged_A_B, merged_C_D)
finish_time = time.clock_gettime_ns(time.CLOCK_REALTIME)


print(merged_list)
print((finish_time - start_time) / 1e9)


