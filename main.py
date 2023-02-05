from pprint import pprint
import re
import csv

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# lastname,firstname,surname,organization,position,phone,email
pattern_phone = r"(8|\+7)\s*[(-]?(\d{3})[)]?\s*[-]?\s*(\d{3})\s*[-]?(\d{2})\s*[-]?(\d{2})(\s*)[(]?(\w+[.])?\s*(\w+)?[)]?"

claen_list = {}
check = []
for contact in contacts_list[1:]:
    text = contact[0] + ' ' + contact[1] + ' ' + contact[2]
    fio = re.split(r'\W+', text)
    phone = re.sub(pattern_phone, r"+7(\2)\3-\4-\5\6\7\8", contact[5])
    check = fio[:3]+contact[3:5]+[phone]+[contact[-1]]
    if fio[0] in claen_list:
        index = 0
        for i in check:
            if i != "":
                claen_list[fio[0]][index] = i
            index +=1
    else: 
        claen_list[fio[0]] = check

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows([i for i in claen_list.values()])

