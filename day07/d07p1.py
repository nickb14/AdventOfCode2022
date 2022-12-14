def main():

    lines = []

    with open("day07/input.txt") as f:
            line = f.readline()
            while line:
                lines.append(line.rstrip())
                line = f.readline()
    
    folders = {}
    name = []

    for line in lines:

        if line[:4] == "$ cd":
            newFolder = line[5:]
            if newFolder == "..":
                name.pop(-1)
            else:
                name.append(newFolder)
                folders[str(name)] = [0]

        elif line != "$ ls":
            last = list(folders)[-1]
            if line[:3] == "dir":
                newName = name.copy()
                newName.append(line[4:])
                folders[last].append(str(newName))
            else:
                folders[last][0] += int(line[:line.find(' ')])
    
    sumOfSmalls = 0
    #reversed so folders within folders are updated first
    for folder, content in reversed(folders.items()):
        size = content[0]
        for i in range(1, len(content)):
            size += folders[content[i]][0]
        folders[folder][0] = size
        #print(folder + ": " + str(size))
        if size <= 100000:
            sumOfSmalls += size
    
    print(sumOfSmalls)


main()