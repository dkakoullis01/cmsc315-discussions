"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================
Author: Dimitrios Kakoullis

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    if 0 <= index < len(lst):
        return lst.pop(index)
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================

    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    print("\n=== INSERTION TESTS ===")
    #list consists of common network service ports like: FTP(21), SSH(22), HTTP(80), HTTPS(443)
    my_list = [21, 22, 80, 443]
    print(f"Original list: {my_list}")
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    #insert at beginning index 0 whihc causes a ful shift right (O(n))
    insert_at(my_list, 0, 53) #DNS Port
    print(f"After inserting DNS port 53 at the beginning: {my_list}")

    #insert in the middle index 2 which shifts elements index 2 and onwards
    insert_at(my_list, 2, 25) #SMTP port
    print(f"After inserting SMTP port 25 in the middle: {my_list}")

    #insert at the end using len (no shifting required)
    insert_at(my_list, len(my_list), 3306) #MySQL port
    print(f"After inserting MySQL port 3306 at the end: {my_list}")
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    #Delete from the beginning
    removed_val = delete_at(my_list, 0)
    print(f"Removed port from beginning: {removed_val}, Updated list: {my_list}")

    #Delete from middle
    removed_val = delete_at(my_list, 2)
    print(f"Removed port from middle: {removed_val}, Updated list: {my_list}")

    #Delete from the end
    removed_val = delete_at(my_list, len(my_list) - 1)
    print(f"Removed port from end: {removed_val}, Updated list: {my_list}")
    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    #search for a value that exists
    search_target = 80
    result_idx = search_value(my_list, search_target)
    print(f"Searching for port {search_target}: Found at index {result_idx}")

    #Search for a value that DOES NOT exist
    search_target = 8080
    result_idx = search_value(my_list, search_target)
    print(f"Searching for port {search_target}: Result is {result_idx} (not found)")
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    #Edge case 1: Delete using an invlaid /out of bounds index
    invalid_delete = delete_at(my_list, 100)
    print(f"Attempting to delete at index 100: returned {invalid_delete} (Safe handling)")

    #Edge case 2: Search for missing value in empty list
    empty_list = []
    empty_search = search_value(empty_list, 21)
    print(f"Searching for port 21 in empty list: returned {empty_search}")

    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")



if __name__ == "__main__":
    main()