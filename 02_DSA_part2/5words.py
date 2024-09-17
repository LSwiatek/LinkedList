with open('5words.txt', 'r') as f:
    list_of_1000_words = words = f.read().splitlines()


def no_repetition(word):
    if len(set(word)) == len(word):
        return True
    else:
        return False


group_of_5 = []
result = []

for word in list_of_1000_words:
    if no_repetition(word) and len(group_of_5) < 5:
        group_of_5.append(word)
    elif no_repetition(word) and len(group_of_5) == 5:
        result.append(group_of_5)
        group_of_5 = []

print(result)


