def main():

    sum = 0

    with open("day04/input.txt") as f:
            line = f.readline()
            while line:

                #this actually looks super unreadable lol eh
                nums = list(map(int, line.replace(',', '-').split('-')))
                if nums[1] >= nums[2] and nums[0] <= nums[3]:
                    sum += 1
            
                line = f.readline()
    
    print(sum)

main()