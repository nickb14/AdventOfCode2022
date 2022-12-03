def main():

    alphabet = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum = 0

    with open("day03/input.txt") as f:
            line = f.readline()
            while line:

                half = len(line)//2
                for i in range(half):
                    a = line[i]
                    if line.count(a, half) > 0:
                        sum += alphabet.find(a)
                        break
            
                line = f.readline()
    
    print(sum)

main()