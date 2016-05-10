def draw_stack(glasses_left, n=1, m=0):
    def draw(glasses, padding):
        print '   ' * padding + ' '.join([' *** '] * glasses) + '   ' * padding
        print '   ' * padding + ' '.join([' * * '] * glasses) + '   ' * padding
        print '   ' * padding + ' '.join([' * * '] * glasses) + '   ' * padding
        print '   ' * padding + ' '.join(['*****'] * glasses) + '   ' * padding

    if glasses_left >= n:
        m = draw_stack(glasses_left - n, n + 1, m)
        draw(m, n - 1)
    return m + 1


N = int(raw_input())
draw_stack(N)
