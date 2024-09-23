import unittest

def find(wordSize, words):
    pass

def test_trivial():
    assert find(2, ['ab', 'cd', 'ef', 'gh', 'ij']) == [['ab', 'cd', 'ef', 'gh', 'ij']]
    assert find(2, ['aa', 'ab', 'cd', 'ef', 'gh', 'ij']) == [['ab', 'cd', 'ef', 'gh', 'ij']]

def test_none_match():
    assert find(2, ['ab', 'ac', 'bc', 'de', 'fg']) == []
    assert find(2, ['ab', 'cc', 'ef', 'gh', 'ij']) == []
    assert find(2, ['aa', 'bb', 'cc', 'dd', 'ee']) == []

def test_size_missmatch():
    assert find(2, ['a', 'b', 'c', 'de', 'fg']) == []
    assert find(2, ['ab', 'ac', 'bc', 'dej', 'fgi']) == []

def test_find_words():
    assert find(2, ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn']) == [
        ['ab', 'cd', 'ef', 'gh', 'ij'],
        ['ab', 'cd', 'ef', 'gh', 'kl'],
        ['ab', 'cd', 'ef', 'gh', 'mn'],
        ['ab', 'cd', 'ef', 'ij', 'kl'],
        ['ab', 'cd', 'ef', 'ij', 'mn'],
        ['ab', 'cd', 'ef', 'kl', 'mn'],
        ['ab', 'cd', 'gh', 'ij', 'kl'],
        ['ab', 'cd', 'gh', 'ij', 'mn'],
        ['ab', 'cd', 'gh', 'kl', 'mn'],
        ['ab', 'cd', 'ij', 'kl', 'mn'],
        ['ab', 'ef', 'gh', 'ij', 'kl'],
        ['ab', 'ef', 'gh', 'ij', 'mn'],
        ['ab', 'ef', 'gh', 'kl', 'mn'],
        ['ab', 'ef', 'ij', 'kl', 'mn'],
        ['ab', 'gh', 'ij', 'kl', 'mn'],
        ['cd', 'ef', 'gh', 'ij', 'kl'],
        ['cd', 'ef', 'gh', 'ij', 'mn'],
        ['cd', 'ef', 'gh', 'kl', 'mn'],
        ['cd', 'ef', 'ij', 'kl', 'mn'],
        ['cd', 'gh', 'ij', 'kl', 'mn'],
        ['ef', 'gh', 'ij', 'kl', 'mn']
    ]


