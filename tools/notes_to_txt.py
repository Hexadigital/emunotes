import json

with open('Notes.json', 'r') as in_file:
    data = json.load(in_file)

txt = ''

for note in data:
    txt += note['Address'] + " - " + note['Note'] + "\n\n"

with open('memory.txt', 'w') as out_file:
    out_file.write(txt)
