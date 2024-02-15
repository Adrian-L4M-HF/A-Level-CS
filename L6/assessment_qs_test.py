from assessment_qs_solutions import mode
from assessment_qs_solutions import rle


def test_mode_normal():
    assert mode([1, 2, 2, 5, 3, 2, 1]) == 3
    assert mode([0, 8, 7, 5, 0, 0, 0]) == 4
    assert mode([9, 9, 9, 8, 8, 7, 7]) == 3


def test_mode_multimodal():
    assert 'modal' in mode([1, 2])
    assert 'modal' in mode([1, 2, 2, 3, 4, 8, 8])
    assert 'modal' in mode([7, 7, 8, 8, 8, 7, 6, 3, 4, 2, 0])


def test_mode_boundary():
    assert mode([0]) == 1
    assert mode([5, 5, 5]) == 3
    assert mode([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == 2


def test_rle_normal():
    assert rle('aaarrrrggghh') == 'a3r4g3h2'
    assert rle('qqquioooppl') == 'q3u1i1o3p2l1'
    assert rle('aabbccddee') == 'a2b2c2d2e2'


def test_rle_boundary():
    assert rle('a') == 'a1'
    assert rle('Z') == 'Z1'


def test_rle_repeated_groups():
    assert rle('cutlasses') == 'c1u1t1l1a1s2e1s1'
    assert rle('zzzqqqiwqooo') == 'z3q3i1w1q1o3'
    assert rle('mississippi') == 'm1i1s2i1s2i1p2i1'
