'''Understanding tuples'''
__author__ = 'Hari'

from placeholders import *

NOTES = '''
Tuples are yet another sequence type along the lines of strings and lists with
its own characteristics.
'''

def test_tuple_type():
    '''testing tuple type'''
    test_tuple = (1,2)   # note the syntax
    assert type(test_tuple).__name__ == 'tuple'

def test_tuple_length():
    '''testing tuple length'''
    colors = ('red', 'blue', 'green')
    assert len(colors) == 3

def test_tuple_with_no_elements():
    '''testing empty tuple'''
    empty = ()
    assert isinstance(empty, tuple) is True
    assert len(empty) == 0

def test_tuple_with_one_element():
    '''testing tuples with single element'''
    test1 = (1)
    assert type(test1).__name__ == 'int'

    test2 = (1,)  #note the syntax used to disambiguate
    assert type(test2).__name__ == 'tuple'

def test_tuple_can_be_indexed():
    '''testing tuples can be indexed'''
    colors = ('red', 'blue', 'green')
    assert colors[0] == 'red'
    assert colors[1] == 'blue'
    assert colors[2] == 'green'

def test_tuple_can_be_sliced():
    '''testing tuples can be sliced'''
    colors = ('red', 'blue', 'green')
    assert colors[1:3] == ('blue', 'green')
    assert colors[1:2] == ('blue',)  #remember the awkward syntax for single element tuples :)


def test_tuples_are_immutable():
    '''testing tuples are immutable'''
    colors = ('red', 'blue', 'green')
    try:
        colors[0] = 'orange'
    except TypeError as exp:
        print (exp) # note the exception -> SyntaxError: Missing parentheses in call to 'print'.
        assert True

def test_tuples_can_be_nested():
    '''testing tuples can contain tuples'''
    top_left = (10,20)
    bottom_right = (40,50)
    rectangle = (top_left, bottom_right)

    assert len(rectangle) == 2
    assert rectangle[0] == (10,20)
    assert rectangle[0][0] == 10
    assert rectangle[1][1] == 50


def test_tuple_unpacking():
    '''test tuple unpacking'''
    pair = (10, 20)
    num_1, num_2 = pair
    assert num_1 == 10
    assert num_2 == 20

    triplet = (10, 20, 30)
    try:
        num_1, num_2 = triplet
        assert False # should not come here.
    except ValueError as v_e:
        print (v_e) # observe what is printed here.
        # In Python 3, printing values changed from being a distinct statement
        # to being an ordinary function call, so it now needs parentheses
        assert True  # ve=>too many values to unpack (expected 2)

def test_sequence_conversion():
    """
    sequences can be converted across forms using the builtin functions.
    """
    word = "testing"
    tup_1 = tuple(word)
    assert tup_1 == ('t','e','s','t','i','n','g')

    list_1 = list(word)
    assert list_1 == ['t','e','s','t','i','n','g']

    list_2 = list(tup_1)
    assert list_2 == ['t','e','s','t','i','n','g']

    word2 = str(tup_1)
    assert word2 == "('t', 'e', 's', 't', 'i', 'n', 'g')"

    word3 = "".join(tup_1)
    assert word3 == 'testing'

    word4 = "".join(list_1)
    assert word4 == 'testing'

THREE_THINGS_I_LEARNT = """
-tuples
-tuple conversions, unpacking
-
"""

TIME_TAKEN_MINUTES = 30
