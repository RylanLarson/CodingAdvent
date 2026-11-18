def main() :

    total = 0

    with open("input.txt") as f:
        lines = f.read().splitlines()

    
    for line in lines:

        digits = list(line.strip())
                
        first_index = 0
        

        for i in range(1, len(digits) - 1):
            
            if digits[i] > digits[first_index]:
                first_index = i

        second_index = first_index + 1

        for j in range(second_index, len(digits)):
            if digits[j] > digits[second_index]:
                second_index = j

        
        total += int(digits[first_index] + digits[second_index])

    print(total)

    
            




if __name__ == "__main__":
    main()