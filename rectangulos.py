def rectangular_panels(a, b, x, y):
    import numpy as np
    """
    Calculate the maximum number of panels of size (a x b) or (b x a) 
    that can fit in a rectangular roof of size (x x y).
    Panels can be placed in mixed configurations.
    int int int int --> int
    """
    grid = [[False] * x for _ in range(y)]

    def can_place(w, h, start_x, start_y):
        if start_x + w > x or start_y + h > y:
            return False
        for yy in range(start_y, start_y + h):
            for xx in range(start_x, start_x + w):
                if grid[yy][xx]:
                    return False
        return True

    def place(w, h, start_x, start_y, val):
        for yy in range(start_y, start_y + h):
            for xx in range(start_x, start_x + w):
                grid[yy][xx] = val

    def next_cell(cx, cy):
        nx = cx + 1
        ny = cy
        if nx >= x:
            nx = 0
            ny = cy + 1
        return nx, ny

    def backtrack(cx, cy):
        if cy == y:
            return 0

        if grid[cy][cx]:
            nx, ny = next_cell(cx, cy)
            return backtrack(nx, ny)

        best = 0
        if can_place(a, b, cx, cy):
            place(a, b, cx, cy, True)
            nx, ny = next_cell(cx, cy)
            best = max(best, 1 + backtrack(nx, ny))
            place(a, b, cx, cy, False)

        if can_place(b, a, cx, cy):
            place(b, a, cx, cy, True)
            nx, ny = next_cell(cx, cy)
            best = max(best, 1 + backtrack(nx, ny))
            place(b, a, cx, cy, False)

        nx, ny = next_cell(cx, cy)
        best = max(best, backtrack(nx, ny))

        return best

    return backtrack(0, 0)

assert(rectangular_panels(0,0,0,0) == 0)
assert(rectangular_panels(1,1,1,1) == 1)
#examples of instructions
assert(rectangular_panels(1,2,2,4) == 4)
assert(rectangular_panels(1,2,3,5) == 7)
assert(rectangular_panels(2,2,1,10) == 0)
#limiting case, vertical is better than mixed
assert(rectangular_panels(3,5,5,9) == 3)
#limiting case, mixed is better than horizontal or vertical
assert(rectangular_panels(2,3,5,5) == 4)
#limiting case, backstracking is better than area method
assert(rectangular_panels(4,5,6,7) == 1)

"""
    Limitaciones:
        1. grillas discretas --> int int int int -> int
        2. Complejidad del algoritmo -> 1x1, O(3^x*y)
"""