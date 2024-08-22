def is_a_subset(arr1: dict, arr2: dict):
    s = set(arr1)
    for n in arr2:
        if n not in s:
            return False
    return True


print(is_a_subset({11, 1, 13, 21, 3, 7}, {11, 3, 7, 1}))
print(is_a_subset({10, 5, 2, 23, 19}, {19, 5, 3}))


def find_intersection_and_union(list1: list, list2: list):
    union_list = list1 + list2
    union_set = set(union_list)
    intersection_list = []
    s1 = set(list1)
    s2 = set(list2)
    for element in s2:
        if element in s1:
            intersection_list.append(element)
    print(f"Intersection List:{intersection_list}. Union List: {union_set}")


find_intersection_and_union([10, 15, 4, 20], [8, 4, 2, 10])
