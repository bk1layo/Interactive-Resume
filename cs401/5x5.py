import sys

class PrimMinimumSpanningTree:

    def primMinimumSpanningTree(self, graph, startVertex):
        numVertices = len(graph)
        visited = [False] * numVertices
        key = [sys.maxsize] * numVertices
        parent = [-1] * numVertices

        key[startVertex] = 0

        for _ in range(numVertices):
            minKey = sys.maxsize
            minVertex = -1

            for v in range(numVertices):
                if not visited[v] and key[v] < minKey:
                    minKey = key[v]
                    minVertex = v

            visited[minVertex] = True

            for v in range(numVertices):
                if (
                    graph[minVertex][v] > 0
                    and not visited[v]
                    and graph[minVertex][v] < key[v]
                ):
                    key[v] = graph[minVertex][v]
                    parent[v] = minVertex

        return parent

    def main(self):
        graph = [
            [0, 13, 2, 1, 15],
            [13, 0, 6, 7, 4],
            [2, 6, 0, 12, 15],
            [1, 7, 12, 0, 16],
            [15, 4, 15, 16, 0]
        ]

        startVertex = 0  # Vertex "a"

        prim = PrimMinimumSpanningTree()
        parent = prim.primMinimumSpanningTree(graph, startVertex)

        totalCost = 0
        for v in range(1, len(parent)):
            totalCost += graph[v][parent[v]]
            print(f"{chr(ord('a') + v)} - {chr(ord('a') + parent[v])}")

        print(f"The cost of the minimum spanning tree is: {totalCost}")


if __name__ == "__main__":
    PrimMinimumSpanningTree().main()
