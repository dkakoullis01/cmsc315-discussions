"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:
Author: Dimitrios Kakoullis

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    #Handle edge case where start node is missing
    if start not in graph:
        print(f"Error: Start node '{start}' not found in graph.")
        return []
    #queue is First-IN-First-OUT(FIFO)
    #This ensures we process all immediate neighbors before moving deeper
    queue = deque([start])

    #Track nodes that have been visted to prevent loops from running forever
    visited = set([start])
    traversal_order = []

    while queue:
        current = queue.popleft()
        traversal_order.append(current)
        #Neighbors are added to queue and appended to get checked level by level
        #Depth-First Search uses a stack (LIFO) to plunge as deep as possible down single path before backtracking
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    #Creating a model of a simple local area network. Nodes represent network hardware(switch, gateway, endpoints)
    #Edges represent ethernet cable or wifi connections between nodes
    network_graph = {
        'Motorola_Gateway': ['Network_Switch', 'Acer_Laptop'],
        'Network_Switch': ['Motorola_Gateway', 'Custom_PC', 'Time_Capsule', 'Formlabs_Printer'],
        'Custom_PC': ['Network_Switch'],
        'Time_Capsule': ['Network_Switch'],
        'Formlabs_Printer': ['Network_Switch'],
        'Acer_Laptop': ['Motorola_Gateway']
    }
    print("\n=== GRAPH STRUCTURE ===")
    for node, edges in network_graph.items():
        print(f"{node} is connected to: {', '.join(edges)}")


# ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    print("\n=== BFS TRAVERSAL ===")

    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("Start BFS from Motorola_Gateway...")
    #BFS visits layer by layer: First the gateway, then switch/laptop, followed by
    #everything connected down the line to the switch
    print("Initial Traversal Order:", bfs(network_graph, 'Motorola_Gateway'))

    print("\nAdding a new Smartphone to the Wi-Fi (connecting to Gateway)... ")
    network_graph['Motorola_Gateway'].append('Smartphone')
    network_graph['Smartphone'] = ['Motorola_Gateway']

    print("Updated Traversal Order:", bfs(network_graph, 'Motorola_Gateway'))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Edge Case 1: Missing Start Node safely handled
    print("Test 1: Starting from a node that doesn't exist (Unknown_Device).")
    bfs(network_graph, 'Unknown_Device')

    # Edge Case 2: Disconnected Graph / Isolated Node
    print("\nTest 2: Adding a disconnected device (Old_Tablet) with no connections.")
    network_graph['Old_Tablet'] = []

    print("Starting BFS from Old_Tablet (should only visit itself):")
    print("Traversal Order:", bfs(network_graph, 'Old_Tablet'))



if __name__ == "__main__":
    main()