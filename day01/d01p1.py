def main():

    m = 0
    c = 0

    with open("day01/input.txt") as f:
            line = f.readline()
            while line:

                if line == '\n':
                    m = max(m, c)
                    c = 0
                else:
                    c += int(line)

                line = f.readline()
    
    print(m)

main()