file = open('demofile.txt', 'r')

lines =0
for line in file:
    lines+=1

print(lines)