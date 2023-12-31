class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        visited = set()
        def bfs():
            q = deque([(0,0,1)])
            visited.add((0,0))
            while q:
                r, c, path_len = q.popleft()
                if r == n-1 and c == n-1:
                    return path_len
                directions = [(-1, 0), (0, -1), (1, 0),(0, 1),(1, -1),(-1, 1),(1,1),(-1, -1)]
                for i, j in directions:
                    if 0<=i+r<n and 0 <=j+c<n and ((i+r, c+j) not in visited) and grid[i+r][c+j] == 0:
                        visited.add((i+r, c+j))
                        q.append((r+i, c+j, path_len + 1))
            return -1
        return bfs()

        