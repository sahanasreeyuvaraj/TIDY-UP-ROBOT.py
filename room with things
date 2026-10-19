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
import matplotlib.pyplot as plt

items = {(1, 5): "red", (5, 2): "blue", (6, 6): "red"}   # item position: color
bins = {"red": (0, 7), "blue": (7, 7)}                   # where each color goes
robot_pos = (0, 0)
carrying = None

def draw():
    plt.cla()                       # clear the picture
    plt.xlim(-0.5, N - 0.5)
    plt.ylim(N - 0.5, -0.5)
    plt.xticks(range(N))
    plt.yticks(range(N))
    plt.grid(True)
    for (x, y) in walls:            # furniture
        plt.plot(x, y, "ks", markersize=30)
    for color, (x, y) in bins.items():   # bins
        plt.plot(x, y, "s", color=color, markersize=30, alpha=0.3)
    for (x, y), color in items.items():  # items left on the floor
        plt.plot(x, y, "o", color=color, markersize=15)
    plt.plot(robot_pos[0], robot_pos[1], "g*", markersize=25)   # robot
    if carrying:                    # show the item it is holding
        plt.plot(robot_pos[0], robot_pos[1], "o", color=carrying, markersize=8)
    plt.pause(0.2)

def walk(goal):
    global robot_pos
    path = bfs(robot_pos, goal)     # find the route
    for cell in path:               # take it one step at a time
        robot_pos = cell
        draw()

for item_pos in list(items.keys()):
    walk(item_pos)                  # go to the item
    carrying = items.pop(item_pos)  # pick it up (it leaves the floor)
    walk(bins[carrying])            # carry it to the matching bin
    carrying = None                 # drop it
    draw()

plt.show()
