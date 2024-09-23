with open('word_trial.txt', 'r') as f:
    list_of_1000_words = words = f.read().splitlines()

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


group_of_5 = []
result = []

for word in list_of_1000_words:
    if len(word) == 2:
        if no_repetition(word) and len(group_of_5) < 5:
            split_word = [char for char in word]
            for char in split_word:
                set_of_used_letters.add(char)
            # set_of_used_letters.add(split_word)
            group_of_5.append(word)
        elif no_repetition(word) and len(group_of_5) == 5:
            result.append(group_of_5)
            group_of_5 = []
            set_of_used_letters = set()
            for char in split_word:
                set_of_used_letters.add(char)
            group_of_5.append(word)

result.append(group_of_5)


# print(group_of_5)
print(result)



