def print_rhombus(n):
    print_up(n)
    print_down(n)


def print_up(n):
    for row in range(1, n + 1):
        for space in range(n - row):
            print(' ', end='')
        for star in range(1, row):
            print('*', end=' ')
        print('*')


def print_down(n):
    for row in range(n - 1, 0, -1):
        for space in range(n - row):
            print(' ', end='')
        for star in range(1, row):
            print('*', end=' ')
        print('*')


n = int(input())
print_rhombus(n)
