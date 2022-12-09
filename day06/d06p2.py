def main():

    num = 14

    with open("day06/input.txt") as f:
            line = f.readline()
    
    for i in range(len(line)-num):
        s = set()
        for x in range(num):
            s.add(line[i+x])
        if len(s) == num:
            print(i+num)
            break
    
main()