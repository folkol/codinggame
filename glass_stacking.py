"""
coding game - glass stacking

triangular numbers: 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55...

n = 30
row   used  left
================
1     1     29
2     3     27
3     6     24
4     10    20
5     15    15
6     21    9
7     28    1
 - done -
"""


def draw_row(n, offset):
    print '   ' * offset + ' '.join([' *** '] * n)
    print '   ' * offset + ' '.join([' * * '] * n)
    print '   ' * offset + ' '.join([' * * '] * n)
    print '   ' * offset + ' '.join(['*****'] * n)


def draw_stack(glasses_left, n=1, offset=0):
    if glasses_left >= n:
        offset = draw_stack(glasses_left - n, n + 1, offset)
        draw_row(offset, n - 1)
    return offset + 1

draw_stack(int(raw_input()))
