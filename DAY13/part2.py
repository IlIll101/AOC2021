def reflect(axis, n, coords, grid):
    n = int(n)
    if axis == 'y':
        for point in coords:
            grid[point[1]][point[0]] -= 1
            point[1] = n - abs(n-point[1])
            grid[point[1]][point[0]] += 1
    elif axis == 'x':
        for point in coords:
            grid[point[1]][point[0]] -= 1
            point[0] = n - abs(n-point[0])
            grid[point[1]][point[0]] += 1

    return coords, grid

def init():
    swap = []
    grid = [[0]*1500 for x in range(1500)]
    coords = [[int(i) for i in x.split(",")] for x in open("input.txt", "r").read().split()]
    folds = open("folds.txt", "r").read().split()
    for i in coords:
        grid[i[1]][i[0]] += 1
    for i in range(len(folds)//3):
        swap.append(folds[(i*3)+2].split("="))
    folds = swap
    return coords, folds, grid

def main():
    coords, folds, grid = init()
    gridr = [len(grid), len(grid[0])]
    for fold in folds:
        coords, grid = reflect(fold[0], fold[1], coords, grid)
        if fold[0] == 'y':
            gridr[0] = int(fold[1])
        elif fold[0] == 'x':
            gridr[1] = int(fold[1])
    for i in range(gridr[0]):
        buffer = ""
        for y in range(gridr[1]):
            if grid[i][y] > 0:
                buffer += "*"
            else:
                buffer += " "
        print(buffer)
       
main()
