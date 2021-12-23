import csv
import re
from pprint import pprint
text = """lastname firstname,surname,organization,position,phone,email
Усольцев Олег Валентинович,,,ФНС,главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц,8 (495) 913-04-78,opendata@nalog.ru
Мартиняхин Виталий Геннадьевич,,,ФНС,,+74959130037,
Наркаев,Вячеслав Рифхатович,,ФНС,,8 495-913-0168,
Мартиняхин,Виталий,Геннадьевич,ФНС,cоветник отдела Интернет проектов Управления информационных технологий,,,
Лукина Ольга Владимировна,,,Минфин,,+7 (495) 983-36-99 доб. 2926,Olga.Lukina@minfin.ru
Паньшин Алексей Владимирович,,,Минфин,,8(495)748-49-73,1248@minfin.ru
Лагунцов Иван Алексеевич,,,Минфин,,+7 (495) 913-11-11 (доб. 0792),
Лагунцов Иван,,,,,,Ivan.Laguntcov@minfin.ru"""

with open('phonebook_raw.csv') as f:
    file = csv.reader(f, delimiter=',')
    file_list = list(file)


# for i in file_list:
#     i[0] = i[0].split()
#     i[0] = (','.join(i[0]))
# print(file_list)

with open('scratch.regexp') as f:
    regex = f.readline()
    regex2 = f.readline()
    regex3 = f.readline()

sub1 = r'+7(\2)\3-\4-\5'
sub2 = r'+7(\2)\3-\4-\5 доб.(\6)'
sub3 = r'\1,\2,\3,'
names = re.compile(regex3.strip())
print(names.findall(text))
with_add = re.compile(regex.strip())
without_add = re.compile(regex2.strip())
res = with_add.sub(sub2, text)
res = without_add.sub(sub1, res, re.MULTILINE)
res = names.sub(sub3, res, re.MULTILINE)
print(res)





tup = tuple()
# print(replaced)
