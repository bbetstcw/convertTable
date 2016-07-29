from markdown import markdown

file = open("input.md", encoding="utf8")

input = file.read()

if input[0]=="|":
    start = 1
else:
    start = 0

file.close()

html = markdown(input)

lines = html[3:len(html)-4].split("\n")

theads = lines[0].split("|")

output = '<table border="1"><thead><tr>\n'

for thead in theads[start:len(theads)-start]:
    output += ("<th>"+thead+"</th>")

output += "\n</tr></thead>"

for line in lines[2:]:
    output += "\n<tr>\n"
    tds = line.split("|")
    for td in tds[start:len(tds)-start]:
        output += ("<td>"+td+"</td>")
    output += "\n</tr>"

output += "\n</table>"

file = open("output.md", "w", encoding="utf8")

file.write(output)

file.close()

print(output)