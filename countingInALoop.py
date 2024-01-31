zork = 0
print('Before', zork)
for thing in [9, 21, 3, -7, 87, 12, 23 * 3]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)