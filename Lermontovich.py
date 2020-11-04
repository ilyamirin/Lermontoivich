import codecs
from random import choice
from datetime import datetime
import re
from tqdm import tqdm


def rhyme_all(rhymes: list) -> list:
    result = list()
    c = 1 # не рифмуем с оригиналом
    for line1 in tqdm(lines):
        for line2 in lines[c:]:
            if line1 == line2:
                continue
            vowels1 = re.findall(r'[уеыаоэяиью]', line1, re.IGNORECASE)
            vowels2 = re.findall(r'[уеыаоэяиью]', line2, re.IGNORECASE)
            if abs(len(vowels1) - len(vowels2)) < 5 and line1[-3:] == line2[-3:]:
                result.append([line1, line2])
        c += 1
    return result


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

all_rhymes = rhyme_all(lines)

f = codecs.open(str(datetime.utcnow().timestamp()) + '.txt', 'w', 'utf-8')
for r in all_rhymes:
    for l in r:
        f.write(l + '\n')
f.close()


