def main():

    fresh_ingrediants = 0

    with open("input.txt") as f:
        ids = f.read().splitlines()

    id_range = []
    id_number = []

    for i in ids:
        
        if "-" in i:
            start, end = map(int, i.split("-"))
            id_range.append((start, end))

        elif i:
            id_number.append(int(i))

    
    for j in id_number:
        for start, end in id_range:

            if j in range(start, end + 1):
                fresh_ingrediants += 1
                break

    print(fresh_ingrediants)

if __name__ == "__main__":
    main()