def main():

    outcomes = { #is there a better way to do this??
        "A X": 3,
        "B X": 1,
        "C X": 2,
        "A Y": 4,
        "B Y": 5,
        "C Y": 6,
        "A Z": 8,
        "B Z": 9,
        "C Z": 7
    }

    score = 0

    with open("day02/input.txt") as f:
            line = f.readline()
            while line:

                score += outcomes[line.rstrip()]

                line = f.readline()
    
    print(score)

main()