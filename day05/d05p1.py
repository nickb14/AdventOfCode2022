def main():

    lines = []

    with open("day05/input.txt") as f:
            line = f.readline()
            while line:
                lines.append(line)
                line = f.readline()
    
    index = lines.index('\n')
    numOfStacks = (len(lines[index-1])) // 4

    stacks = []
    bottomRow = lines[index-2]
    for j in range(numOfStacks):
        stacks.append([bottomRow[j*4+1]])
    for i in range(index-2): #I assumed that there are only single digit stack numbers
        row = lines[index-3-i] #this algorithm was going to be so good in my brain... but alas so many restrictions
        for j in range(numOfStacks):
            crate = row[j*4+1]
            if crate != ' ':
                stacks[j].append(crate)

    procedure = lines[index+1:]
    for line in procedure:
        space = line.find(" from")
        m = int(line[5:space])
        f = int(line[space+6]) - 1 #indexing be like
        t = int(line[space+11]) - 1 #also singel digit things...
        for x in range(m):
            stacks[t].append(stacks[f].pop())
    
    final = ""
    for stack in stacks:
        final += stack[-1]
    print(final)

main()