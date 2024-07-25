import random

list1 = [1, 4, 2, 6, 1, 9, 13, 10, 33, 12, 0]
list2 = [1, 4, 2, 6, 1, 9, 13, 10, 33, 12, 0]

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list3 =[]
for i in range(100):
    r_letter = random.choice(letters)
    list3.append(r_letter)

print(list3)

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


def find_word(list):
    pass


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
    sorted_words_dict = sorted(words_dict.items(), key=lambda x : x[1], reverse=True)
    print(words_list)
    print(sorted_words_dict)


print(div_by_2(list1))
print(find_2nd_highest(list2))
print(find_repetition(list4))
find_repetition_in_text()
