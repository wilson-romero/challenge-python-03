import re
from functools import reduce
# Resolve the problem!!


def run():
    # Start coding here
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        pattern = '[a-z]+'
        mapped = map(lambda line: re.findall(pattern, line), f.readlines())
        characters = reduce((lambda string, character: character), mapped)
        result = ''.join(characters)
        print(result)


if __name__ == '__main__':
    run()
