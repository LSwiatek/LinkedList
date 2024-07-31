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
    second = list[0]
    for n in list:
        if n > highest:
            second = highest
            highest = n
        elif highest > n > second:
            second = n
    return second


def list_duplicates_of(list, item):
    index_list = []
    start = 0
    for i in list:
        if i == item:
            index_list.append(start)
        start += 1
    return index_list


# list = ["a", "s", "t"]
# for i in range(0, len(list)-1):
#     if list[i] == "a" and list[i+1] == "b" and list[i+2] == "b" and list[i+3] == "a":
#         return i


def find_abba(list):
    if "a" in list:
        a_index_list = list_duplicates_of(list,"a")
        for element in a_index_list:
            a_index = element
            if list[a_index+1] == "b" and list[a_index+2] == "b" and list[a_index+3] == "a":
                return a_index
    else:
        print("abba not present in the list")


# def find_word_in_list(list, word):
#     n = len(word)
#     new_list = list(word)
#
#     for i in range(0, len(list)-1):
#         for j in range(0,n-1):
#             if list[i] == new_list[j] and list[i+1] == new_list[j+1] and list[i+2] == "b" and list[i+3] == "a":
#                 return f"starting at index {i}"
#
#     # for i in range(len(letters_list) - n + 1):
#     #     if list[i:i+n] == new_list:
#     #         return f"starting at index {i}"
#
#     return "not found"


def find_repetition(list):
    first = []
    repeated = []
    for element in list:
        if element in first and element not in repeated:
            repeated.append(element)
        elif element not in first:
            first.append(element)
    return repeated


def find_repetition_in_text():
    text = input("Insert text: ")
    words_list = text.split()
    words_dict = {}
    for word in words_list:
        if word not in words_dict:
            words_dict[word] = 1
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


# fib(10)


# print(f"Numbers dividable by 2 are: {div_by_2(list1)}")
# print(f"The second highest number is: {find_2nd_highest(list2)}")
# print(f"The repetitions in the list are: {find_repetition(list4)}")
# print(f"The repetitions in the text are: {find_repetition_in_text()}")
# print(f"ABBA is at index {find_abba(list3)} of the list")
# print(f"Your word is {find_word_in_list(list3, "abba")}")
print(list_duplicates_of(list3,"a"))


