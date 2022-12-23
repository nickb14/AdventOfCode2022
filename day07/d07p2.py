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
    
    #this just updates folders within folders, so that content[0] is the accurate total size
    for folder, content in reversed(folders.items()):
        size = content[0]
        for i in range(1, len(content)):
            size += folders[content[i]][0]
        folders[folder][0] = size
    
    sizes = []
    for content in folders.values():
        sizes.append(content[0])
    sizes.sort()

    minimumSize = sizes[-1] - (70000000-30000000)
    for size in sizes:
        if minimumSize < size:
            print(size)
            break


main()