def main():

    lines = []
    
    with open("day09/input.txt") as f:
        line = f.readline()
        while line:
            lines.append(line)
            line = f.readline()
    
    #me continuing to disrespect Python's usabliity
    xH, yH, xT, yT = 0, 0, 0, 0
    allTPos = set()

    for line in lines:
        dir = line[0]
        num = int(line[2:])

        for i in range(num):
            #yes I am checking the same thing multipple times what about it º_º
            if dir == 'R':
                xH += 1
            elif dir == 'L':
                xH -= 1
            elif dir == 'U':
                yH += 1
            else: #if dir == 'D':
                yH -= 1
            
            #ok but I really hope I don't have to return to this becaause this is no less than a complete mess of code XD
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
            
            allTPos.add((xT, yT))
    
    #YAHAHA it actually worked first try I'm not even kidding I'm dead lmao
    #ok what is wrong with me
    print(len(allTPos))


main()