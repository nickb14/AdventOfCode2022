def main():

    grid = [] #assumed square
    
    with open("day08/input.txt") as f:
        line = f.readline()
        while line:
            grid.append(list(map(int, line.rstrip())))
            line = f.readline()
    
    maxScore = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            tree = grid[i][j]

            #me writing the ugliest code possible be like

            #up
            up = 0
            x = i-1
            while x >= 0:
                up += 1
                if grid[x][j] >= tree:
                    break
                x -= 1
            
            #down
            down = 0
            x = i+1
            while x < rows:
                down += 1
                if grid[x][j] >= tree:
                    break
                x += 1

            #left
            left = 0
            x = j-1
            while x >= 0:
                left += 1
                if grid[i][x] >= tree:
                    break
                x -= 1

            #right
            right = 0
            x = j+1
            while x < cols:
                right += 1
                if grid[i][x] >= tree:
                    break
                x += 1

            score = up*down*left*right
            maxScore = max(maxScore, score)

    
    print(maxScore)

main()