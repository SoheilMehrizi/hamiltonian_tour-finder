import networkx as nx
import matplotlib.pyplot as plt

def hamiltonian_tour(adj_matrix, start):
    n = len(adj_matrix)
    visited = [False] * n
    path = [start[0]]
    min_cost = float('inf')
    best_path = []

    def backtrack(curr, cost, count):
        nonlocal min_cost, best_path
        if count == n:
            if adj_matrix[curr][start[0]] != 0:
                total_cost = cost + adj_matrix[curr][start[0]]
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_path = path.copy()
        for i in range(n):
            if not visited[i] and adj_matrix[curr][i] != 0:
                visited[i] = True
                path.append(i)
                backtrack(i, cost + adj_matrix[curr][i], count + 1)
                visited[i] = False
                path.pop()

    visited[start[0]] = True
    backtrack(start[0], 0, 1)

    tour = [(best_path[i], best_path[i + 1]) for i in range(len(best_path) - 1)] + [(best_path[-1], start[0])]
    return tour

def visualize_tour(adj_matrix, tour):
    G = nx.Graph()
    n = len(adj_matrix)

    G.add_nodes_from(range(n))

    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] != 0:
                G.add_edge(i, j, weight=adj_matrix[i][j])

    pos = nx.spring_layout(G, seed=42)  # Consistent layout
    edge_colors = ['red' if (u, v) in tour or (v, u) in tour else 'gray' for u, v in G.edges()]
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, edge_color=edge_colors, node_color='skyblue', node_size=1000, font_size=14)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Hamiltonian Tour (Shortest Path)")
    plt.show()

# Example usage
adj_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
start_element = (0, 1)

tour = hamiltonian_tour(adj_matrix, start_element)
print("Optimal Tour:", tour)
visualize_tour(adj_matrix, tour)
