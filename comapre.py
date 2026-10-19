from collections import deque
from itertools import permutations
import random
import matplotlib.pyplot as plt

N = 8
walls = {(3, 1), (3, 2), (3, 3), (3, 4)}
bins = {"red": (0, 7), "blue": (7, 7)}
START = (0, 0)

cache = {}   # remembers distances so we don't recompute them

def dist(a, b):
    """Number of steps from cell a to cell b, going around furniture (BFS)."""
    if (a, b) in cache:
        return cache[(a, b)]
    q = deque([(a, 0)])
    seen = {a}
    while q:
        (x, y), d = q.popleft()
        if (x, y) == b:
            cache[(a, b)] = d
            return d
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in walls and (nx, ny) not in seen:
                seen.add((nx, ny))
                q.append(((nx, ny), d + 1))
    return None

def cost(order, items):
    """Total steps to tidy the items in the given order."""
    pos = START
    total = 0
    for p in order:
        bin_pos = bins[items[p]]
        total += dist(pos, p)        # walk to the item
        total += dist(p, bin_pos)    # carry it to its bin
        pos = bin_pos
    return total

def random_strategy(items):
    order = list(items)
    random.shuffle(order)
    return cost(order, items)

def nearest_strategy(items):
    pos = START
    remaining = list(items)
    order = []
    while remaining:
        nxt = min(remaining, key=lambda p: dist(pos, p))
        order.append(nxt)
        remaining.remove(nxt)
        pos = bins[items[nxt]]
    return cost(order, items)

def best_strategy(items):
    return min(cost(order, items) for order in permutations(items))

def random_items(k):
    free = [(x, y) for x in range(N) for y in range(N)
            if (x, y) not in walls and (x, y) not in bins.values() and (x, y) != START]
    spots = random.sample(free, k)
    return {s: random.choice(["red", "blue"]) for s in spots}

random.seed(1)
trials = 100
totals = {"Random": 0, "Nearest first": 0, "Best possible": 0}

for _ in range(trials):
    items = random_items(6)          # a new messy room each time
    totals["Random"] += random_strategy(items)
    totals["Nearest first"] += nearest_strategy(items)
    totals["Best possible"] += best_strategy(items)

names = list(totals.keys())
averages = [totals[n] / trials for n in names]

for n, a in zip(names, averages):
    print(n + ":", round(a, 1), "steps on average")

saving = (averages[0] - averages[1]) / averages[0] * 100
print("Nearest first uses", round(saving), "% fewer steps than random")

plt.bar(names, averages, color=["gray", "green", "gold"])
plt.ylabel("Average steps to tidy 6 items")
plt.title("Tidy-up robot: strategy comparison (100 random rooms)")
plt.savefig("results.png")
plt.show()