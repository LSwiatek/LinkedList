def bowling_score(array: list):
    score = 0
    i = 0
    frames = 10
    for frame in range(frames):
        if array[i] == 10:
            score += 10 + array[i+1] + array[i+2]
            i += 1
        elif i + 1 < len(array) and array[i] + array[i+1] == 10:
            score += 10 + array[i+2]
            i += 2
        else:
            score += array[i] + array[i+1]
            i += 2
    return score


def test_regular_score():
    assert bowling_score([8, 1, 4, 2, 3, 5, 0, 5, 1, 3, 2, 2, 9, 0, 2, 5, 1, 1, 2, 5]) == 61
    assert bowling_score([5, 0, 4, 4, 2, 7, 0, 0, 8, 1, 4, 2, 2, 5, 1, 1, 2, 5, 6, 3]) == 62


def test_spare():
    assert bowling_score([8, 2, 4, 2, 3, 5, 0, 5, 1, 3, 2, 2, 9, 0, 2, 5, 1, 1, 2, 5]) == 66
    assert bowling_score([5, 0, 4, 4, 3, 7, 5, 0, 8, 1, 4, 2,2, 5, 1, 1, 2, 5, 6, 3]) == 73


def test_strike():
    assert bowling_score([8, 1, 10, 3, 5, 0, 5, 1, 3, 2, 2, 9, 0, 2, 5, 1, 1, 2, 5]) == 73
    assert bowling_score([5, 0, 4, 4, 2, 7, 0, 0, 8, 1, 4, 2, 2, 5, 10, 2, 5, 6, 3]) == 77


test_regular_score()
test_strike()
test_spare()

print(bowling_score([1 ,3, 10, 0, 0, 5, 5, 3, 1, 7, 2, 9, 0, 10, 3, 3, 6, 2]))
print(bowling_score([5, 5, 4, 0, 8, 1, 10, 0, 10, 1, 10, 4, 6, 10, 10, 5]))
