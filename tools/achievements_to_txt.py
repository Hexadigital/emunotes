import json

with open('data.json', 'r') as in_file:
    data = json.load(in_file)

txt = ''

for ach in data['Achievements']:
    txt += ach['Title'] + "\n" + ach['Description'] + " [" + str(ach['Points']) + "]\n" + ach["MemAddr"] + "\n\n"

with open('achievements.txt', 'w') as out_file:
    out_file.write(txt)
