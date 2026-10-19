from collections import deque

N = 8
walls = {(3, 1), (3, 2), (3, 3), (3, 4)}   # furniture

def bfs(start, goal):
    q = deque([(start, [start])])
    seen = {start}
    while q:
        (x, y), path = q.popleft()
        if (x, y) == goal:
            return path
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in walls and (nx, ny) not in seen:
                seen.add((nx, ny))
                q.append(((nx, ny), path + [(nx, ny)]))
    return None

print(bfs((0, 0), (6, 5)))