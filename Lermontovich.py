import codecs
from datetime import datetime
import re
from tqdm import tqdm


def is_rhyme(string1: str, string2: str) -> bool:
    vowels1 = re.findall(r'[уеыаоэяиью]', string1, re.IGNORECASE)
    vowels2 = re.findall(r'[уеыаоэяиью]', string2, re.IGNORECASE)
    return abs(len(vowels1) - len(vowels2)) < 5 and string1[-3:] == string2[-3:]


def pair_all(pairs: list) -> list:
    result = list()
    c = 0
    for pair1 in tqdm(pairs):
        for pair2 in pairs[c:]:
            if pair1[0] == pair2[0]:
                continue
            if is_rhyme(pair1[0], pair2[0]) and is_rhyme(pair1[1], pair2[1]):
                result.append([pair1, pair2])
        c += 1
    return result


def rhyme_all(rhymes: list) -> list:
    result = list()
    c = 1
    for line1 in tqdm(lines):
        for line2 in lines[c + 2:]:
            if line1 == line2:
                continue
            if is_rhyme(line1, line2):
                result.append([line1, line2])
        c += 1
    return result


f = codecs.open('Библия.txt', 'r')
lines = list(map(lambda l: re.sub(r'[,\.\-\—\:!\?"]', '', l).strip(), f.readlines()))
f.close()

lines = list(map(lambda l: re.sub(r'\[[0-9\–]+\]', '', l), lines))
lines = list(filter(lambda l: len(l) > 2, lines))
lines = list(filter(lambda l: l.count('html') == 0, lines))

all_rhymes = rhyme_all(lines)

pairs = pair_all(all_rhymes)

f = codecs.open(str(datetime.utcnow().timestamp()) + '.txt', 'w', 'utf-8')
for r in all_rhymes:
    for l in r:
        f.write(l + '\n')
f.close()


