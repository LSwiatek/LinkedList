list1 = [1, 4, 2, 6, 1, 5, 8]
list2 = [ 1, 3, 5, 7, 8, 9, 8, 6, 4, 3, 2]
list3 = ["abdgf", "eeeeeeeee", "abdlgrl", "aaa"]

def find_subtractions_for_result(list, number):
    results = ()
    for i in list:
        for j in range(0, len(list)):
            if i - list[j] == number:
                results += i, list[j]
    print(results)

find_subtractions_for_result(list1, 3)


def find_highest_number(list):
    highest = list[0]
    for i in list:
        if i > highest:
            highest = i
    return highest


print(find_highest_number(list2))

