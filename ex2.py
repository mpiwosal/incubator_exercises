import re

file = open("commands.txt", "r")
pattern = "^switchport trunk allowed vlan (.*)"
all_vlans = []

for line in file.readlines():
    result = re.match(pattern, line)
    if result is not None:
        myList = result.group(1).split(',')
        # to strip spaces
        for i in range(0, myList.__len__()):
            myList[i] = myList[i].strip()
        # to remove duplicates
        all_vlans.append(list(set(myList)))

vlans = {}
for i in range(0, all_vlans.__len__()):
    current_list = all_vlans[i]
    for j in range(0, current_list.__len__()):
        current_el = current_list[j]
        if current_el in vlans.keys():
            vlans[current_el] = vlans[current_el] + 1
        else:
            vlans[current_el] = 1

unique = []
common = []
for key in vlans:
    if vlans[key] == 1:
        unique.append(key)
    if vlans[key] == all_vlans.__len__():
        common.append(key)

print("unique: " + str(unique))
print("common: " + str(common))
