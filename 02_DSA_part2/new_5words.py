with open("5_letter_words.txt", "r") as text:
    list_of_5_letter_words_no_rep = text.read().splitlines()


def find_groups_of_5_words(list_of_words):
    used_letters = []
    result = []
    groups_of_5 = []
    for i in range(len(list_of_words)):
        for j in range(i, len(list_of_words)):
            repeating = False
            for letter in list_of_words[j]:
                if letter in used_letters:
                    repeating = True
                    break
            if not repeating:
                result.append(list_of_words[j])
                for letter in list_of_words[j]:
                    used_letters.append(letter)
        if len(result) == 5:
            groups_of_5.append(result)
            print(result)
            result.clear()
        print(used_letters)
        print(result)
        used_letters.clear()
        result.clear()

    return result, groups_of_5


print(find_groups_of_5_words(list_of_5_letter_words_no_rep))
