jj = 24
kk = jj % 5
print(kk)


astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
    print(istr)