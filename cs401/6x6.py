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
            [0, 45, 11, 66, 76, 1],
            [45, 0, 55, 77, 88, 3],
            [11, 55, 0, 23, 90, 5],
            [66, 77, 23, 0, 53, 43],
            [76, 88, 90, 53, 0, 67],
            [1, 3, 5, 43, 67, 0]
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
