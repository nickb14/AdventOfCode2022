def main():

    with open("day06/input.txt") as f:
            line = f.readline()
    
    for i in range(len(line)):
        set = {line[i], line[i+1], line[i+2], line[i+3]} #mega scuffed
        if len(set) == 4:
            print(i+4)
            break
    
main()