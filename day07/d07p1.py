def main():

    lines = []

    with open("day07/input.txt") as f:
            line = f.readline()
            while line:
                lines.append(line.rstrip())
                line = f.readline()
    
    folders = {"/": [0]}

    for line in lines:

        if line[:4] == "$ cd":
            newFolder = line[5:]
            if newFolder != "..":
                folders[newFolder] = [0]

        elif line != "$ ls":
            last = list(folders)[-1]
            if line[:3] == "dir":
                folders[last].append(line[4:])
            else:
                folders[last][0] += int(line[:line.find(' ')])
    
    sumOfSmalls = 0
    for folder, content in folders.items():
        size = content[0]
        for i in range(1, len(content)):
            size += folders[content[i]][0]
        if size <= 100000:
            print(folder + ": " + str(size))
            sumOfSmalls += size
    
    print(sumOfSmalls)


main()