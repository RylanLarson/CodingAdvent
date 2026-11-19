def main() :

    total = 0

    with open("input.txt") as f:
        lines = f.read().splitlines()

    
    for line in lines:

        digits = list(line.strip())
                
        first_index = 0
        

        for i in range(1, len(digits) - 11):
            
            if digits[i] > digits[first_index]:
                first_index = i

        second_index = first_index + 1

        for i in range(second_index, len(digits) - 10):
            if digits[i] > digits[second_index]:
                second_index = i
        
        third_index = second_index + 1
        for i in range(third_index, len(digits) - 9):
            if digits[i] > digits[third_index]:
                third_index = i

        fourth_index = third_index + 1
        for i in range(fourth_index, len(digits) - 8):
            if digits[i] > digits[fourth_index]:
                fourth_index = i

        fifth_index = fourth_index + 1
        for i in range(fifth_index, len(digits) - 7):
            if digits[i] > digits[fifth_index]:
                fifth_index = i

        sixth_index = fifth_index + 1
        for i in range(sixth_index, len(digits) - 6):
            if digits[i] > digits[sixth_index]:
                sixth_index = i

        seventh_index = sixth_index + 1
        for i in range(seventh_index, len(digits) - 5):
            if digits[i] > digits[seventh_index]:
                seventh_index = i

        eighth_index = seventh_index + 1
        for i in range(eighth_index, len(digits) - 4):
            if digits[i] > digits[eighth_index]:
                eighth_index = i

        ninth_index = eighth_index + 1
        for i in range(ninth_index, len(digits) - 3):
            if digits[i] > digits[ninth_index]:
                ninth_index = i 

        tenth_index = ninth_index + 1
        for i in range(tenth_index, len(digits) - 2):
            if digits[i] > digits[tenth_index]:
                tenth_index = i

        eleventh_index = tenth_index + 1
        for i in range(eleventh_index, len(digits)-1):
            if digits[i] > digits[eleventh_index]:
                eleventh_index = i

        twelve_index = eleventh_index + 1
        for i in range(twelve_index, len(digits)):
            if digits[i] > digits[twelve_index]:
                twelve_index = i
        
        total += int(digits[first_index] + digits[second_index] + digits[third_index] + digits[fourth_index] + digits[fifth_index] + digits[sixth_index] + digits[seventh_index] + digits[eighth_index] + digits[ninth_index] + digits[tenth_index] + digits[eleventh_index] + digits[twelve_index])

    print(total)

    
            




if __name__ == "__main__":
    main()