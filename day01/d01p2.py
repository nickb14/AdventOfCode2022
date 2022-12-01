def main():

    calories = []
    c = 0

    with open("day01/input.txt") as f:
            line = f.readline()
            while line:

                if line == '\n':
                    calories.append(c)
                    calories.sort(reverse=True)
                    calories = calories[:3]
                    c = 0
                else:
                    c += int(line)

                line = f.readline()
    
    print(calories[0] + calories[1] + calories[2])

main()