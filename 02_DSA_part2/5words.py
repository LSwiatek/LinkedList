with open('5words.txt', 'r') as f:
    list_of_1000_words = f.read().splitlines()


def find_words(wordSize, words):
    group_of_5 = []
    result = []
    set_of_used_letters = set()

    def no_repetition(word):
        not_repeated = False
        if len(set(word)) == len(word):
            not_repeated = True
            list_of_letters_in_word = [char for char in word]
            for char in list_of_letters_in_word:
                if char in set_of_used_letters:
                    not_repeated = False
                    break
        return not_repeated

    for word in words:
        if len(word) == int(wordSize):
            if no_repetition(word) and len(group_of_5) < 4:
                split_word = [char for char in word]
                for char in split_word:
                    set_of_used_letters.add(char)
                # set_of_used_letters.add(split_word)
                group_of_5.append(word)
            elif no_repetition(word) and len(group_of_5) == 4:
                split_word = [char for char in word]
                for char in split_word:
                    set_of_used_letters.add(char)
                group_of_5.append(word)
                result.append(group_of_5)
                group_of_5 = []
                set_of_used_letters = set()

    print(result)
    print(group_of_5)


# def test_trivial():
#     assert find_words(2, ['ab', 'cd', 'ef', 'gh', 'ij']) == [['ab', 'cd', 'ef', 'gh', 'ij']]
#     assert find_words(2, ['aa', 'ab', 'cd', 'ef', 'gh', 'ij']) == [['ab', 'cd', 'ef', 'gh', 'ij']]
#
#
# test_trivial()

# def test_none_match():
#     assert find_words(2, ['ab', 'ac', 'bc', 'de', 'fg']) == []
#     assert find_words(2, ['ab', 'cc', 'ef', 'gh', 'ij']) == []
#     assert find_words(2, ['aa', 'bb', 'cc', 'dd', 'ee']) == []
#
#
# test_none_match()

# find_words(2, ['aa', 'ab', 'cd', 'ef', 'gh', 'ij'])

# def find_words_of_legnth_without_repeating_letter(length, list_of_words):
#     result = []
#     for word in list_of_words:
#         if len(word) == length:
#             if len(set(word)) == len(word):
#                 result.append(word)
#     for word in result:
#         print(word)
#
# print(find_words_of_legnth_without_repeating_letter(5, list_of_1000_words))

with open("5_letter_words.txt", "r") as text:
    list_of_5_letter_words = text.read().splitlines()










