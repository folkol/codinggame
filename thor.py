
directions = {
    (-1, -1): 'NW',
    (0, -1): 'N',
    (1, -1): 'NE',
    (1, 0): 'E',
    (1, 1): 'SE',
    (0, 1): 'S',
    (-1, 1): 'SW',
    (-1, 0): 'W'
}

light_x, light_y, thor_x, thor_y = [int(i) for i in raw_input().split()]

while True:
    remaining_turns = int(raw_input())  # The remaining amount of turns Thor can move. Do not remove this line.

    from numpy import sign
    dx, dy = sign(light_x - thor_x), sign(light_y - thor_y)
    print directions[(dx, dy)]
    thor_x, thor_y = dx, dy
