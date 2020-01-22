from left_join import left_join


def test_left_join_one():
    map1 = {
        'fond': 'enamored',
        'wrath': 'anger',
        'diligent': 'employed',
        'outfit': 'garb',
        'guide': 'usher',
    }
    map2 = {
        'fond': 'averse',
        'wrath': 'delight',
        'diligent': 'idle',
        'guide': 'follow',
        'flow': 'jam',
    }
    actual = []
    actual = left_join(map1, map2)
    expected = [
        ['fond', 'enamored', 'averse'],
        ['wrath', 'anger', 'delight'],
        ['diligent', 'employed', 'idle'],
        ['outfit', 'garb', None],
        ['guide', 'usher', 'follow']
    ]
    assert actual == expected

def test_left_join_two():
    map1 = {
        'happy': 'glad',
        'sad': 'unhappy',
        'busy': 'occupied',
        'big': 'huge',
        'small': 'tiny',
    }
    map2 = {
        'small': 'big',
        'big': 'small',
        'nice': 'bad',
        'fun': 'boring',
        'bright': 'dim',
    }
    actual = []
    actual = left_join(map1, map2)
    expected = [
        ['happy', 'glad', None],
        ['sad', 'unhappy', None],
        ['busy', 'occupied', None],
        ['big', 'huge', 'small'],
        ['small', 'tiny', 'big']
        ]
    assert actual == expected

def test_left_join_number():
    map1 = {
        1: 'glad',
        3: 22.3,
        6: 'occupied',
        15: 'huge',
        23: 'tiny',
    }
    map2 = {
        3: 'big',
        15: 44,
        28: 'bad',
        5: 'boring',
        44: 'dim',
    }
    actual = []
    actual = left_join(map1, map2)
    expected = [
        [1, 'glad', None],
        [3, 22.3, 'big'],
        [6, 'occupied', None],
        [15, 'huge', 44],
        [23, 'tiny', None]
        ]
    assert actual == expected
