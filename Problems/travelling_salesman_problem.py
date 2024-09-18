import time
import random

cities = ['A', 'B', 'C', 'D']
cities_distance = {
    'A': {'B': 199, 'C': 196, 'D': 450},
    'B': {'A': 199, 'C': 287, 'D': 263},
    'C': {'A': 196, 'B': 287, 'D': 542},
    'D': {'A': 450, 'B': 263, 'C': 542},
}


def tsp(cities, cities_distance):
    visited = set()
    start = random.choice(cities)
    visited.add(start)
    route = [start]
    total_distance = 0
    in_city = route[0]
    while len(visited) < len(cities):
        min_distance = float('inf')
        min_city = None
        for city in cities:
            if city not in visited:
                distance = cities_distance[in_city][city]
                if distance < min_distance:
                    min_distance = distance
                    target_city = city
                    visited.add(target_city)
                    route.append(target_city)
                    in_city = target_city
    return route


if __name__ == '__main__':
    start = time.time()
    print(tsp(cities, cities_distance))
    print(time.time() - start)
