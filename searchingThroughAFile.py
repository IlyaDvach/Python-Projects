fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('milk'):
        print(line)