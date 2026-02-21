def gridChallenge(grid):
    # Step 1: sort each row
    sorted_grid = [''.join(sorted(row)) for row in grid]

    n = len(sorted_grid)
    m = len(sorted_grid[0])

    # Step 2: check columns
    for col in range(m):
        for row in range(n - 1):
            if sorted_grid[row][col] > sorted_grid[row + 1][col]:
                return "NO"

    return "YES"