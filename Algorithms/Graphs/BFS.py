graph = {
    "Amin": {"Wasim", "Nick", "Mike"},
    "Wasim": {"Imran", "Amin"},
    "Imran": {"Wasim", "Faras"},
    "Faras": {"Imran"},
    "Mike": {"Amin"},
    "Nick": {"Amin"},
}


def bfs(graph: dict[str, set], start: str) -> set:
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)

    return visited


if __name__ == '__main__':
    print(bfs(graph, "Amin"))
