from typing import List

def split(data: str, sep=None, maxsplit=-1):
    if data.isspace():  # check if input string contains only whitespace characters
        return [data]
    return data.strip().split(sep, maxsplit)

# Test the function
data = '    Hi     Python    world!   '
print(split(data))  # Output: ['Hi', 'Python', 'world!']


if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']