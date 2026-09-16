

"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================
Author: Dimitrios Kakoullis

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

import time

def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    #Linear search has O(n) time complexity because in scenario where data set is large
    #it must check every single element in list one by one. If list has 'n' elements, it take 'n' operations to locate target
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1



def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST (Network Ports) ===")
    print("TODO: Create a small dataset and test both searches.")
    port_list = [21, 22, 25, 53, 80 , 443, 3389, 8080]
    target_found = 443 #HTTPS (Exists)
    target_missing = 23 #Telnet (Does not exist/blocked)

    #targets found by linear and binary search
    print(f"Active Ports Dataset: {port_list}")
    print(f"Linear Search for Port {target_found}: Found at index {linear_search(port_list, target_found)}")
    print(f"Binary Search for Port {target_found}: Found at index {binary_search(port_list, target_found)}")

    #missing targets by lienar and binary search
    print(f"Linear Search for Port {target_missing}: Result {linear_search(port_list, target_missing)}")
    print(f"Binary Search for Port {target_missing}: Result {binary_search(port_list, target_missing)}")
    # ===============================
    # TODO (Student): LARGE DATASET (Packet Sequence IDs)
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST (Packet Sequence IDs)===")
    #Creating a sorted list of 1 million packet sequence numbers
    print("TODO: Create a larger dataset and compare results.")
    packet_list = list(range(1000000))
    target_packet = 999999 #worst case scenario

    #measure time of linear search
    start_time = time.perf_counter()
    linear_result = linear_search(packet_list, target_packet)
    linear_time = time.perf_counter() - start_time

    #measure time of binary search
    start_time = time.perf_counter()
    binary_result = binary_search(packet_list, target_packet)
    binary_time = time.perf_counter() - start_time

    print(f"Searching for Packet ID {target_packet} in a log of 1,000,000 packets:")
    print(f"Linear Search found it at index {linear_result} in {linear_time:.6f} seconds")
    print(f"Binary Search found it at index {binary_result} in {binary_time:.6f} seconds")

    print("Conclusion: Binary search is drastically faster for large packet logs because it elminates half the remaining logs with every check.")
    # ===============================
    # TODO (Student): EDGE CASES Tests
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")
    #Edge case 1 : Empty list for no open ports
    empty_ports = []
    print(f"Edge Case 1 (Empty Port list search for Port 80):")
    print(f"Linear Result: {linear_search(empty_ports, 80)}")
    print(f"Binary Result: {binary_search(empty_ports, 80)}")
    print("Both linear and binary return -1 safely without crashing because their loop conditions crash immediately ")

    #Edge Case 2: Single Element List
    single_port = [22]
    print(f"\nEdge Case 2 (Single Port List search for Port 22):")
    print(f"Linear Result: {linear_search(single_port, 22)}")
    print(f"Binary Result: {binary_search(single_port, 22)}")
    print("Both algorithms correctly handle a list of size 1 and find index at 0.")

if __name__ == "__main__":
    main()