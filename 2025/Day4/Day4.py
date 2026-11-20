def main():

    rolls_removed = 0
    can_remove = True
    
    with open("input.txt") as f:
        grid = [list(line.strip()) for line in f]

    while True:

        removed_this_pass = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):

                if grid[r][c] == ".":
                    continue

                adjacentRolls = 0
                            
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        
                        if dr == 0 and dc == 0:
                            continue

                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "@":
                            adjacentRolls += 1
                                      
                        
                if adjacentRolls < 4:
                    rolls_removed += 1
                    removed_this_pass += 1
                    grid[r][c] = '.'
                                 
            
        if removed_this_pass == 0:
            break

    print(rolls_removed)
    

if __name__ == "__main__":
    main()
