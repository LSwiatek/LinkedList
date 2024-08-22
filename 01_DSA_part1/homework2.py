list1 = [1, 4, 2, 6, 1, 5, 8]
list2 = [1, 3, 5, 7, 8, 9, 8, 6, 4, 3, 2, 0]
string1 = "ABCDEFGABEF"


def find_subtractions_for_result(list, number):
    results = []
    for i in list:
        for j in range(0, len(list)):
            if i - list[j] == number:
                results.append((i, list[j]))
    return results


print(find_subtractions_for_result(list1, 3))


def find_highest_number(list):
    i = 0
    while list[i] < list[i+1]:
        i += 1
    return list[i]


print(find_highest_number(list2))


class Repetition:

    def __init__(self):
        list_of_strings = []
        index = None

    def __str__(self):
        return f'Repetition(list_of_strings={self.list_of_strings}, index={self.index})'

    def __repr__(self):
        return self.__str__()


def find_longest_substring_without_rep():
    text = input("Insert text: ")
    input_list = list(text)
    list_of_repetitions = []
    r = Repetition()
    r.list_of_strings = []
    r.index = 0
    counter = 0
    for element in input_list:
        if element not in r.list_of_strings:
            r.list_of_strings.append(element)
        else:
            list_of_repetitions.append(r)
            r = Repetition()
            r.list_of_strings = [element]
            r.index = counter
        counter += 1
    list_of_repetitions.append(r)
    result = []
    for elem in list_of_repetitions:
        if len(result) < len(elem.list_of_strings):
            result = elem.list_of_strings
            result_index = elem.index
    return list_of_repetitions, result, result_index


def find_longest_substring_without_rep2():
    text = input("Insert text: ")
    input_list = list(text)
    length = len(input_list)
    max_length = 0
    result = []
    result_index = 0
    for element in input_list:
        visited = []
        index = input_list.index(element)
        for i in range(index, length):
            if input_list[i] not in visited:
                visited.append(input_list[i])
            elif input_list[i] in visited:
                break
        if len(visited) > max_length:
            max_length = len(visited)
            result.clear()
            result.append(visited)
            result_index = index
    print(f"The longest string without repetitions is {result}, with length of {max_length}, starting at index {result_index}")


# print(find_longest_substring_without_rep())
find_longest_substring_without_rep2()




