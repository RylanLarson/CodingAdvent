def main():

    rollsMoved = 0
    
    with open("input.txt") as f:
        grid = [line.strip() for line in f]

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
                rollsMoved += 1

            

    print(rollsMoved)
    

if __name__ == "__main__":
    main()
