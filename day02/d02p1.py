def main():

    outcomes = {
        "A X": 4,
        "B X": 1,
        "C X": 7,
        "A Y": 8,
        "B Y": 5,
        "C Y": 2,
        "A Z": 3,
        "B Z": 9,
        "C Z": 6
    }

    score = 0

    with open("day02/input.txt") as f:
            line = f.readline()
            while line:

                score += outcomes[line.rstrip()]

                line = f.readline()
    
    print(score)

main()