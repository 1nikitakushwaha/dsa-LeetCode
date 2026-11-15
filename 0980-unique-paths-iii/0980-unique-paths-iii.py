class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
   
        rows, cols = len(grid), len(grid[0])

        # scan: find the start, count the 0-cells that must be covered
        empty = 0
        sr = sc = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    empty += 1
                elif grid[r][c] == 1:
                    sr, sc = r, c

        def dfs(r, c, remaining):
            # 1. out of bounds, obstacle, or already visited
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1:
                return 0

            # 2. reached the end: valid only if every 0-cell was covered
            if grid[r][c] == 2:
                return 1 if remaining == 0 else 0

            # 3. stepping onto a 0-cell uses one up
            if grid[r][c] == 0:
                remaining -= 1

            # 4. choose: mark visited
            temp = grid[r][c]
            grid[r][c] = -1

            # 5. explore: add up the counts from all 4 directions
            total = (dfs(r + 1, c, remaining) +    # down
                     dfs(r - 1, c, remaining) +    # up
                     dfs(r, c + 1, remaining) +    # right
                     dfs(r, c - 1, remaining))     # left

            # 6. un-choose: restore the original value (0 or 1)
            grid[r][c] = temp
            return total

        return dfs(sr, sc, empty)
        