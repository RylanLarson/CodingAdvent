def main():
    print("Hello, World!")


    numsZero = 0
    currentVal = 50


    with open("input.txt") as f:
        lines = f.read().splitlines()


    for amount in lines:
        userDirection = amount[0]
        userNumber = int(amount[1:])

        if userDirection == "R":
            currentVal += userNumber

        if userDirection == "L":
            currentVal -= userNumber

        while currentVal > 99:
            currentVal -= 100

        while currentVal < 0:
            currentVal += 100 

        if currentVal == 0:
            numsZero += 1

    print(numsZero)
    

if __name__ == "__main__":
    main()