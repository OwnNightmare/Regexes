import csv
import re
from pprint import pprint

with open('phonebook_raw.csv') as f:
    file = csv.reader(f, delimiter=',')
    file_list = list(file)

for i in range(len(file_list)):
    file_list[i] = ','.join(file_list[i])
text = '\n'.join(file_list)

with open('scratch.regexp') as f:
    regex = f.readline()
    regex2 = f.readline()
    regex3 = f.readline()


def make_regexes():
    sub1 = r'+7(\2)\3-\4-\5'
    sub2 = r'+7(\2)\3-\4-\5 доб.(\6)'
    sub3 = r'\1,\2,'
    names = re.compile(regex3.strip())
    with_add = re.compile(regex.strip())
    without_add = re.compile(regex2.strip())
    res = with_add.sub(sub2, text)
    res = without_add.sub(sub1, res, re.MULTILINE)
    res = names.sub(sub3, res)
    return res


def remove_empties(source=make_regexes()):
    _pack = []
    new_result = []
    source = source.split(sep='\n')
    for i in source:
        i = i.split(sep=',')
        _pack.append(i)
    for i in _pack:
        if len(i) > 7:
            for n in range(len(i) - 7):
                i.remove('')
    for i in _pack:
        rec = ','.join(i)
        new_result.append(rec)
    new_result = '\n'.join(new_result)
    return new_result


with open('new.csv', 'w') as f:
    result = remove_empties()
    f.write(result)


def unite_duplicated():
    pack = []
    outer_list = []
    with open('new.csv') as f:
        substrings = [line.strip().split(sep=',') for line in f]
        print(substrings)
    for index, substring in enumerate(substrings):
        step = 1
        while index + step < len(substrings):
            if substrings[index][0:2] == substrings[index + step][0:2]:
                a = index
                b = index + step
                tup = (a, b)
                pack.append(tup)
            step += 1
    zipped_pack = []
    originals = []
    duplicates = []
    for tup in pack:
        _original = tup[0]
        _duplicate = tup[1]
        originals.append(_original)
        duplicates.append(_duplicate)
        zipped = list(zip(substrings[_original], substrings[_duplicate]))
        zipped_pack.append(zipped)
    for index, zipped in enumerate(zipped_pack):
        inner_list = []
        for tup in zipped:
            if tup[0] == tup[-1]:
                inner_list.append(tup[0])
            elif tup[0] != tup[-1]:
                if tup[-1] != '':
                    inner_list.append(tup[1])
                else:
                    inner_list.append(tup[0])
        outer_list.append(inner_list)
    for i in range(len(outer_list)):
        outer_list[i] = ', '.join(outer_list[i])
    return outer_list, originals, duplicates


def make_substitutions(args, string=result):
    index = 0
    resulting_list = []
    list_, orig_indexes, dup_indexes = args
    split_result = string.split(sep='\n')
    for i in orig_indexes:
        split_result[i] = list_[index]
        index += 1
    removing_list = []
    for i in dup_indexes:
        removing_list.append(split_result[i])
    for string in removing_list:
        split_result.remove(string)
    for string in split_result:
        resulting_list.append(string.split(','))
    return resulting_list


result = make_substitutions(unite_duplicated())
with open('new.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(result)

