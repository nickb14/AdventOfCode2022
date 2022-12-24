def main():

    grid = [] #assumed square
    
    with open("day08/input.txt") as f:
        line = f.readline()
        while line:
            grid.append(list(map(int, line.rstrip())))
            line = f.readline()
    
    total = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            tree = grid[i][j]

            #me writing the ugliest code possible be like

            #up
            visible = True
            x = i-1
            while x >= 0:
                if grid[x][j] >= tree:
                    visible = False
                x -= 1
            if visible == True:
                total += 1
                continue #if it is visible one way, then it is visible period
            
            #down
            visible = True
            x = i+1
            while x < rows:
                if grid[x][j] >= tree:
                    visible = False
                x += 1
            if visible == True:
                total += 1
                continue

            #left
            visible = True
            x = j-1
            while x >= 0:
                if grid[i][x] >= tree:
                    visible = False
                x -= 1
            if visible == True:
                total += 1
                continue

            #right
            visible = True
            x = j+1
            while x < cols:
                if grid[i][x] >= tree:
                    visible = False
                x += 1
            if visible == True:
                total += 1
                continue
    
    print(total)

main()