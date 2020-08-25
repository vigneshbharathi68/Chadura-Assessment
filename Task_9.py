with open('test.txt.txt', 'r') as f:
    for i, line in enumerate(f, start=1):
        print('{}={}'.format(i, line.strip()))


