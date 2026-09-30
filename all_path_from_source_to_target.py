class all_path_from_source_to_target:
    def all_path_from_source_to_target(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        result = []

        def backtrack(node, path):
            if node == target:
                result.append(list(path))
                return

            for next_node in graph[node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()
        path = 0
        backtrack(0, path)
        return result

    # Complexity - O(2^N . N)
    # Space complexity - O(N)