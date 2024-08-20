list1 = [1, 5, 4, 6, 3, 9, 6]
list2 = [1, 5, 4, 6, 3, 9, 6]
list3 = [1, 5, 4, 6, 3, 9, 6]
list4 = [1, 5, 4, 6, 3, 9, 6]


def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def insert_sort(list):
    n = len(list)
    if n <= 1:
        return
    for i in range(1, n):
        j = i - 1
        temp = list[i]
        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp
    return list


def quick_sort(list):
    n = len(list)
    if n <= 1:
        return list
    pivot = list[n//2]
    left = [x for x in list if x < pivot]
    right = [x for x in list if x > pivot]
    middle = [x for x in list if x == pivot]
    return quick_sort(left) + middle + quick_sort(right)


def part_left(list):
    n = len(list)
    if n <= 1:
        return list
    else:
        middle = n // 2
        left = list[:middle]
        return left


def part_right(list):
    n = len(list)
    if n <= 1:
        return list
    else:
        middle = n // 2
        right = list[middle:]
        return right


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


print(f"Bubble sorted list: {bubble_sort(list1)}")
print(f"Insert sorted list: {insert_sort(list2)}")
print(f"Quick sorted list: {quick_sort(list3)}")
print(part_left(list4))
print(part_right(list4))
