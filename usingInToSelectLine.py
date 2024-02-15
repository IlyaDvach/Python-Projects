fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not 'milk' in line:
        continue
    print(line) 