from practice_qs import prime_checker as q1
from practice_qs import word_in_word as q2


def test_Q1_normal():
    candidate_nos = [3, 4, 5, 6, 7, 8, 9, 10, 11]
    results = [True, False, True, False, True, False, False, False, True]
    assert q1(candidate_nos) == results


def test_Q1_boundary():
    assert q1([0, 1]) == [False, False]


def test_Q1_erroneous():
    assert q1([-1, 0.5, 11.9]) == [False, False, False]


def test_Q2_normal():
    assert q2('eat', 'ate')
    assert q2('eat', 'heart')
    assert q2('to', 'position')


def test_Q2_boundary():
    assert not q2('meet', 'meat')
    assert not q2('meaty', 'meat')
    assert not q2('abcdeee', 'aaabcdee')


def test_Q2_erroneous():
    assert not q2('abc', 'def')
    assert not q2('dog', 'bad')
    assert not q2('cat', 'dog')


print(test_Q1_normal())
print(test_Q1_boundary())
print(test_Q1_erroneous())
print(test_Q2_normal())
print(test_Q2_boundary())
print(test_Q2_erroneous())
