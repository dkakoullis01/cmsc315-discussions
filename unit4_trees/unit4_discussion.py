"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================
Author: Dimitrios Kakoullis

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        #Insertion depends on comparing values to maintain BST rule where smaller values
        #must go left and larger values must go right.
        #This structure is what allows future searches to skip half the tree.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        #Finding the empty slot/insertion position
        if node is None:
            return Node(value)

        #Goes down the subtree based on BST ordering rule it recurds down tree either left or right
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            pass

        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        #BST search is more efficeint than linear search (O(n)) because each comparsion
        #eliminates up to half of remaining nodes resulting in O(log n) time complexity for balanced tree
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False
        if node.value == value:
            return True
        #Target is small -->traverse LEFT, target is large-->traverse RIGHT
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)


    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        #In-order traversal visits left child which is smaller
        #In-order traversal visits root
        #In-order traversal visits right child which is larger
        #Conforms with BST rules which means output will process in ascending order.
        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION (Network Ports) ===")
    bst = BST()

    #Decided to insert common network port numbers
    #To start, I will use port 80 (HTP) as the root distributes common ports across both subtrees
    #LEFT SIDE will consist of all the lwoer port numbers such as: 22 (SSH), 21 (FTP), 53 (DNS), 25 (SMTP)
    #RIGHT SIDE wil cotnain all higher port numbers such as 443 (HTTPS), 3389 (RDP), 8080 (HTTP-Alt)
    #BST seems like an idea choice as each node comparison during a firewall lookup will immideatly remove
    #up to half of the remaining port numbers
    network_ports = [80, 22, 443, 21, 53, 3389, 8080, 25]
    print(f"Network ports to insert: {network_ports}")

    for port in network_ports:
        bst.insert(port)
    print("Port routing tree built succesfully")
    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    #In-order traversal (left-node-right) processes the ports in ascending order.
    #Recursivly exausts all lower port numbers on the left branches before it actually records the current port,
    #then visits the higher port numbers on right branch
    sorted_ports = bst.inorder()
    print(f"In-Order traversal (sequential ports): {sorted_ports}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    #Existing ports: 25 (SMTP - left subtree) and 3389 (RDP - right subtree)
    # Path to 25: 80 -> 22 -> 53 -> 25 (True)
    # Path to 3389: 80 -> 443 -> 3389 (True)
    existing_queries = [25, 3389]
    for port in existing_queries:
        found = bst.search(port)
        print(f"Port {port} lookup: {'OPEN' if found else 'BLOCKED'}")

    # Non-existing ports: 23 (Telnet) and 67 (DHCP)
    # Path for 23: 80 -> 22 -> 53 -> 25 -> Left is None (False)
    # Path for 67: 80 -> 22 -> 53 -> Right is None (False)
    missing_queries = [23, 67]
    for port in missing_queries:
        found = bst.search(port)
        print(f"Port {port} lookup: {'OPEN' if found else 'BLOCKED'}")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    #Edge case 1: searching an empty firewall rule set
    #This search method must handle root == None gracefully without throwing an error
    empty_firewall = BST()
    print(f"Empty tree traversal: {empty_firewall.inorder()} (expected: [])")
    print(f"Lookup port 110 (POP3) in empty tree: {empty_firewall.search(110)} (expected: False)")

    #Edge case 2: Duplicate port insertion
    #Re-inserting port 80 (HTTP) where BST logic will simply pass right over it
    #which prevents duplicate rules from cluttering the data structure.
    bst.insert(80)
    print(f"Traversal after duplicate inserion of port 80: {bst.inorder()} (length remains 8)")


if __name__ == "__main__":
    main()