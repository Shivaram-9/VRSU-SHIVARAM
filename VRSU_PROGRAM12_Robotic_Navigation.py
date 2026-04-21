import heapq

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    visited = set()

    while open_list:
        cost, node = heapq.heappop(open_list)

        print("Visiting:", node)

        if node == goal:
            print("Goal Reached!")
            return

        visited.add(node)

        neighbors = [node + 1, node - 1]

        for n in neighbors:
            if n not in visited:
                heapq.heappush(open_list, (cost + 1, n))

astar(0, 5)
