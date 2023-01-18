def main():

    lines = []
    
    with open("day09/input.txt") as f:
        line = f.readline()
        while line:
            lines.append(line)
            line = f.readline()
    
    xs, ys = [0]*10, [0]*10
    all9Pos = set()

    for line in lines:
        dir = line[0]
        num = int(line[2:])

        for i in range(num):
            if dir == 'R':
                xs[0] += 1
            elif dir == 'L':
                xs[0] -= 1
            elif dir == 'U':
                ys[0] += 1
            else: #if dir == 'D':
                ys[0] -= 1
            
            for j in range(9):
                pos = move(xs[j], ys[j], xs[j+1], ys[j+1])
                xs[j+1] = pos[0]
                ys[j+1] = pos[1]
            
            all9Pos.add((xs[9], ys[9]))

    print(len(all9Pos))

#just straight up stolen from p1, moved into a new function
def move(xH, yH, xT, yT):
    xDif = xH - xT
    yDif = yH - yT
    if xDif == 2:
        xT += 1
        if yDif == 2 or yDif == 1:
            yT += 1
        elif yDif == -1 or yDif == -2:
            yT += -1
    elif xDif == 1:
        if yDif == 2:
            xT += 1
            yT += 1
        elif yDif == -2:
            xT += 1
            yT += -1
    elif xDif == 0:
        if yDif == 2:
            yT += 1
        elif yDif == -2:
            yT += -1
    elif xDif == -1:
        if yDif == 2:
            xT += -1
            yT += 1
        elif yDif == -2:
            xT += -1
            yT += -1
    if xDif == -2:
        xT += -1
        if yDif == 2 or yDif == 1:
            yT += 1
        elif yDif == -1 or yDif == -2:
            yT += -1
    
    return (xT, yT)

main()