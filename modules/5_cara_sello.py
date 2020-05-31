import random

numberOfStreaks = 0
result = ''
head_count = 0
tail_count = 0
for i in range(10000):
    head_or_tail = random.randint(0,1)
    if head_or_tail == 0:
        head_count += 1
        if head_count == 6:
            numberOfStreaks += 1
        result += 'H'
        tail_count = 0
    else:
        tail_count += 1
        if tail_count == 6:
            numberOfStreaks += 1
        result += 'T'
        head_count = 0

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))