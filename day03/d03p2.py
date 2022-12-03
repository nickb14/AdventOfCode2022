def main():

    alphabet = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum = 0

    sacks = [None, None, None]

    with open("day03/input.txt") as f:
            for i in range(3):
                sacks[i] = f.readline()
            while sacks[2]:

                for i in range(len(sacks[0])):
                    a = sacks[0][i]
                    if sacks[1].count(a) > 0 and sacks[2].count(a) > 0:
                        sum += alphabet.find(a)
                        break

                for i in range(3):
                    sacks[i] = f.readline()
    
    print(sum)

main()