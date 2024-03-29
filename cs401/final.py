import sys

class ShortestPathWithSequence:

    def find_shortest_path(self, distance_graph, sequence_graph, start_vertex, end_vertex):
        num_vertices = len(distance_graph)
        visited = [False] * num_vertices
        distance = [sys.maxsize] * num_vertices
        parent = [-1] * num_vertices

        distance[start_vertex] = 0

        for _ in range(num_vertices):
            min_distance = sys.maxsize
            min_vertex = -1

            for v in range(num_vertices):
                if not visited[v] and distance[v] < min_distance:
                    min_distance = distance[v]
                    min_vertex = v

            visited[min_vertex] = True

            for v in range(num_vertices):
                if (
                    not visited[v]
                    and distance_graph[min_vertex][v] > 0
                    and distance[min_vertex] + distance_graph[min_vertex][v] < distance[v]
                ):
                    distance[v] = distance[min_vertex] + distance_graph[min_vertex][v]
                    parent[v] = min_vertex

        # Reconstruct the shortest path
        path = []
        current_vertex = end_vertex
        while current_vertex != -1:
            path.insert(0, current_vertex)
            current_vertex = parent[current_vertex]

        return path, distance[end_vertex]

    def main(self):
        distance_graph = [
            [0, 1, 3, 1, 4],
            [8, 0, 3, 2, 5],
            [10, 11, 0, 4, 7],
            [6, 7, 2, 0, 3],
            [3, 4, 7, 4, 0]
        ]

        sequence_graph = [
            [0, 1, 3, 3, 3],
            [4, 1, 2, 3, 3],
            [4, 4, 2, 3, 3],
            [4, 4, 2, 3, 4],
            [0, 0, 1, 0, 4]
        ]

        start_vertex = 0  # Starting vertex (e.g., 'a')
        end_vertex = 1    # Ending vertex (e.g., 'e')

        path, shortest_distance = self.find_shortest_path(distance_graph, sequence_graph, start_vertex, end_vertex)

        if shortest_distance == sys.maxsize:
            print(f"No path found from {chr(ord('a') + start_vertex)} to {chr(ord('a') + end_vertex)}")
        else:
            path_names = [chr(ord('a') + vertex) for vertex in path]
            print(f"Shortest path from {chr(ord('a') + start_vertex)} to {chr(ord('a') + end_vertex)}:")
            print(" -> ".join(path_names))
            print(f"Shortest distance: {shortest_distance}")

            # Print all vertices visited along the path
            print(f"Vertices visited along the path: {', '.join([chr(ord('a') + vertex) for vertex in path])}")


if __name__ == "__main__":
    ShortestPathWithSequence().main()
