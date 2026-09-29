"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================
Author: Dimitrios Kakoullis
STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    #create copy of original list
    arr = lst.copy()
    n = len(arr)

    #loop entire list
    for i in range(n):
        swapped = False
        #compare adjacent elements
        for j in range(0, n - i - 1):
            #swap elements out of order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        #stop early if already sorted
        if not swapped:
            break
    #return sorted list
    return arr


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    #If list has 1 or 0 elements, has been sorted
    if len(lst) <= 1:
        return lst

    #divide list into smaller halves
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    #sort each half recursively
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    #merge sorted halves together and then return
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    #compare values from left and right lists
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    #Append any remaining values
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    vm_memory_allocations = [8192, 1024, 4096, 2048, 16384, 512, 6144]
    print(f"Original VM RAM Allocations (MB): {vm_memory_allocations}")
    print(f"Bubble Sorted: {bubble_sort(vm_memory_allocations)}")
    print(f"Merge Sorted: {merge_sort(vm_memory_allocations)}")

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")
    #Simulating a secondary much larger database server cluster
    db_cluster_ram = [32768, 8192, 16384, 4096, 8192, 2048, 6144, 10240, 12288]
    print(f"Original DB Cluster RAM (MB): {db_cluster_ram}")
    print(f"Bubble Sorted: {bubble_sort(db_cluster_ram)}")
    print(f"Merge Sorted: {merge_sort(db_cluster_ram)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element listcd
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")
    empty_cluster = []
    #Edge case 1 is empty list
    print("\nEdge Case: Empty List (0 VMs online")
    print(f"Original: {empty_cluster} -> Merge Sorted: {merge_sort(empty_cluster)}")
    print("The algorithms handle this without fail since there is nothign left to iterate or divide.")

    #Edge case 2: List already sorted
    optimized_cluster = [1024, 2048, 4096, 8192, 16384]
    print("\nEdge Case: Already Sorted List")
    print(f"Original: {optimized_cluster} -> Bubble Sorted: {bubble_sort(optimized_cluster)} ")
    print("Bubble sort works great here because of swapped boolean flag being used, it makes a single pass to see no swaps made, breaks out early. ")

    #Edge Case 3: List with duplicate values
    duplicate_ram = [4096, 4096, 4096, 4096]
    print("\nEdge Case: Duplicates (Identical VM Templates)")
    print(f"Original: {duplicate_ram} -> Merge Sorted: {merge_sort(duplicate_ram)}")
    print("By using the '<=' operator in our merge function, it maintains stability and keeps identical values in order ")


if __name__ == "__main__":
    main()