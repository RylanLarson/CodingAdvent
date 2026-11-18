def main():

    invalidTotal = 0

    with open("test.txt") as f:
        raw_IDs = f.read().strip().split(",")


    for id_range in raw_IDs:

        at_index = id_range.index("-")  
        start = int(id_range[:at_index])
        end = int(id_range[at_index + 1:])

        for n in range(start, end ):
            num = str(n)

            if len(num) % 2 != 0:
                continue

            mid = len(num) // 2

            if num[:mid] == num[mid:]:
                invalidTotal += n

        
        
    print(invalidTotal)

    return raw_IDs


if __name__ == "__main__":
    main()