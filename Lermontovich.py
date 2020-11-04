import codecs
from random import choice
from datetime import datetime
import re
from tqdm import tqdm


def rhyme_double(rhymes: list, match: int) -> list:
    result = list()
    result.append(choice(rhymes))
    while len(result) < 2:
        idea = choice(lines)
        if idea == result[-1]:
            continue
        vowels1 = re.findall(r'[уеыаоэяиью]', idea, re.IGNORECASE)
        vowels2 = re.findall(r'[уеыаоэяиью]', result[-1], re.IGNORECASE)
        if abs(len(vowels1) - len(vowels2)) < 5 and idea[-match:] == result[-1][-match:]:
            result.append(idea)
    return result


f = codecs.open('Маяковский  Владимир . Полное собрание сочинений в тринадцати томах. Том первый. Стихотворения (1912-1917) - royallib.ru.txt', 'r')
lines = list(map(lambda l: l.strip(), f.readlines()))
f.close()

lines = list(filter(lambda l: len(l) > 2, lines))

f = codecs.open(str(datetime.utcnow().timestamp()) + '.txt', 'w')
for i in range(10):
    print(rhyme_double(lines, 3))
f.close()


