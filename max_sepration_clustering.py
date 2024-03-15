from scipy.spatial import distance
from collections import defaultdict

def create_edges(points):
    """Generates a list of edges represented as tuples (distance, point1, point2)."""
    edges = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance.euclidean(points[i], points[j])
            edges.append((dist, i, j))
    return edges

def find(parent, i):
    """Finds the root of the set that element i belongs to."""
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    """Unites two sets that elements x and y belong to."""
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def k_max_clusters(k, points):
    """Forms k maximally separated clusters from the given points."""
    edges = create_edges(points)
    edges.sort()  # Sort edges based on distance
    
    # Kruskal's MST construction
    parent = [i for i in range(len(points))]
    rank = [0 for _ in range(len(points))]
    
    mst = []
    for edge in edges:
        dist, u, v = edge
        uroot = find(parent, u)
        vroot = find(parent, v)
        if uroot != vroot:
            mst.append((u, v))
            union(parent, rank, uroot, vroot)
    
    # Remove k-1 longest edges from the MST
    mst_edges = [(u, v, distance.euclidean(points[u], points[v])) for u, v in mst]
    mst_edges_sorted_by_dist = sorted(mst_edges, key=lambda x: x[2], reverse=True)
    for edge in mst_edges_sorted_by_dist[:k-1]:
        mst.remove((edge[0], edge[1]))

    # Reinitialize parent for cluster identification
    parent = [i for i in range(len(points))]
    for u, v in mst:
        union(parent, rank, u, v)
    
    # Assign points to clusters based on their final parent
    cluster_ids = {find(parent, i): [] for i in range(len(points))}
    for i, point in enumerate(points):
        cluster_ids[find(parent, i)].append(point)
    
    return list(cluster_ids.values())

# Example usage with the specified sample input
k = 2
points = [
    (1, 2), (10, 2), (1, 0),
    (10, 0), (1, 1), (10, 1)
]

clusters = k_max_clusters(k, points)
print(clusters)
