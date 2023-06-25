from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]


def bfs_v1(graph):
    people = deque()
    people += graph["you"]

    searched = []

    while people:
        person = people.popleft()

        if not person in searched:
            if len(person) > 3:
                print("Found")
                return True
            else:
                people += graph[person]

        searched += person

    return False


print(bfs_v1(graph))
