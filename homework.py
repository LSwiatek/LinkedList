import random

list1 = [1, 4, 2, 6, 1, 9, 13, 10, 33, 12, 0]
list2 = [1, 4, 2, 6, 1, 9, 13, 10, 33, 12, 0]

list3 = ["a", "c", "d", "e", "x", "z", "a", "b", "b", "a", "z", "s", "a", "b", "b", "a", "z"]

list4 = ["ab", "ac", "ad", "ar", "ac", "ax", "aw", "ab", "ab"]


def div_by_2(list):
    new_list = []
    for n in list:
        if n % 2 == 0:
            new_list.append(n)
    return new_list


def find_2nd_highest(list):
    highest = list[0]
    second = list [0]
    for n in list:
        if n > highest:
            second = highest
            highest = n
        elif highest > n > second:
            second = n
    return second


def list_duplicates_of(list, item):
    start_at = -1
    index_list = []
    while True:
        try:
            index = list.index(item, start_at+1)
        except ValueError:
            break
        else:
            index_list.append(index)
            start_at = index
    return index_list


def find_abba(list):
    if "a" in list:
        a_index_list = list_duplicates_of(list,"a")
        for element in a_index_list:
            a_index = element
            if list[a_index+1] == "b" and list[a_index+2] == "b" and list[a_index+3] == "a":
                return a_index
    else:
        print("abba not present in the list")


def find_repetition(list):
    first = []
    repeated = []
    for element in list:
        if element in first and element not in repeated:
            repeated.append(element)
        else:
            first.append(element)
    return repeated


def find_repetition_in_text():
    text = input("Insert text: ")
    words_list = text.split()
    words_dict = {}
    for word in words_list:
        if word not in words_dict:
            words_dict[word] = 0
        elif word in words_dict:
            words_dict[word] += 1
    sorted_words_dict = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_words_dict

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n < 0:
        raise Exception("Value must be positive")
    return fib(n - 1) + fib(n - 2)


fib(10)


print(f"Number dividable by 2 are: {div_by_2(list1)}")
print(f"The second highest number is: {find_2nd_highest(list2)}")
print(f"The repetitions in the list are: {find_repetition(list4)}")
print(f"The repetitions in the text are: {find_repetition_in_text()}")
print(f"ABBA is at index {find_abba(list3)} of the list")
