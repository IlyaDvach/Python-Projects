count = 0
sum = 0
print('Before', count, sum)
for value in [9, 12, 15, 3 - 7, 3 * 7, 2^2]:
    count = count + 1
    sum = sum + count
    print(count, sum, value)
print('After', count, sum, sum / count)