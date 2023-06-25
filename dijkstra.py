# Graph hashtable setup
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["Fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["Fin"] = 5
graph["Fin"] = {}

# Costs hashtable setup
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["Fin"] = float("inf")

# Parents hashtable setup
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["Fin"] = None

processed = []


def dijkstra():
    node = get_cheapest_node(costs)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]

            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node

        processed.append(node)
        node = get_cheapest_node(costs)

    return costs


def get_cheapest_node(costs):
    cheapest_cost = float('inf')
    cheapest_node = None

    for node in costs:
        cost = costs[node]

        if cost < cheapest_cost and node not in processed:
            cheapest_cost = cost
            cheapest_node = node

    return cheapest_node

print(get_cheapest_node(costs))
