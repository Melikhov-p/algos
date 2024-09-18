graph = {
    "Amin": {"Wasim", "Nick", "Mike"},
    "Wasim": {"Imran", "Amin"},
    "Imran": {"Wasim", "Faras"},
    "Faras": {"Imran"},
    "Mike": {"Amin"},
    "Nick": {"Amin"},
}


def dfs(graph: dict[str, set], start: str, visited: set = None) -> set:
    if not visited:
        visited = set()
    visited.add(start)
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)

    return visited


if __name__ == '__main__':
    print(dfs(graph, 'Amin'))
