fname = input('Enter the file name:  ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('milk'):
        count = count + 1
print('There were', count, 'subject lines in', fname )

#You need Download file 'mbox.txt' and write it in the input