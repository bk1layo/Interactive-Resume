def g(i, cities):
    if len(cities) == 0:
        return c[i][0]  # Base case: If no cities left to visit, return to the starting city (index 0)

    min_cost = float('inf')
    for k in cities:
        remaining_cities = set(cities)
        remaining_cities.remove(k)

        # Recursive call
        cost = c[i][k] + g(k, remaining_cities)
        min_cost = min(min_cost, cost)

    return min_cost

def tsp(graph):
    num_cities = len(graph)
    all_cities = list(range(num_cities))

    def get_cost(mask, pos):
        if mask == (1 << num_cities) - 1:
            return graph[pos][0]  # Return to the starting city

        min_cost = float('inf')
        for city in range(num_cities):
            if (mask & (1 << city)) == 0:
                new_mask = mask | (1 << city)
                cost = graph[pos][city] + get_cost(new_mask, city)
                min_cost = min(min_cost, cost)

        return min_cost

    return get_cost(1, 0)  # Start from the first city (0) with mask 1

c = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0],
]

start_city = 1  # Adjust index to match matrix indices (0-based)
cities_to_visit = set([2,3])  # Adjust city numbers to match matrix indices
min_cost = g(start_city, cities_to_visit)
# min_cost = tsp(c)
print("Minimum Cost:", min_cost)  # Output the minimum cost
