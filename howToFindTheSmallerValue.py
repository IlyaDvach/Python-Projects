small = None
print('Before', small)
for num in [9, 41, 12, 3, 74, 15]:
    if small is None:
        small = num
    if num < small:
        small = num
    print(small, num)
print('After', small)

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)