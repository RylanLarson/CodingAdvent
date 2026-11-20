def main():

    fresh_ingrediants = 0
    freshID_range = 0

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

    
    # for j in id_number:
    #     for start, end in id_range:

    #         if j in range(start, end + 1):
    #             fresh_ingrediants += 1

    #             valid_range = end - start

    #             for k in range(valid_range):
    #                 freshID_range += 1

    #             break

    id_range.sort()
    total = 0
    cur_start, cur_end = id_range[0]

    for start, end in id_range[1:]:
        if start <= cur_end:
            cur_end = max(cur_end, end)
        else:
            total += cur_end - cur_start + 1
            cur_start, cur_end = start, end

    total += cur_end - cur_start + 1
    print(total)
      
    

    

if __name__ == "__main__":
    main()