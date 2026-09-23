"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================
Author: Dimitrios Kakoullis

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")
    #Python dictionaries behave like hash tables by taking a unique key(host name) and
    #running it through a hashing function, and finaly storing value (IP address) at specific memory index
    vm_network = {
        "Ubuntu-Server-01": "10.0.0.5",
        "Windows11-Web-01": "10.0.0.12",
        "Rhel-Web-02": "10.0.0.20",
        "Fedora-Test": "10.0.0.25",
        "Ubuntu-DesktopGUI": "10.0.0.30"
        }
    print("Initial VM Network Allocations:")
    print(vm_network)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.


    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")
    #Lookups are O(1) time complexity because system computes hash of hostname and goes directly
    #to that memory address instead of scanning whole network list/DHCP server
    ubuntu_ip = vm_network["Ubuntu-Server-01"]
    windows_ip = vm_network["Windows11-Web-01"]

    print(f"IP Allocation for Ubuntu-Server-01: {ubuntu_ip}")
    print(f"IP Allocation for Windows11-Web-01: {windows_ip}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")
    #When assigning new IP to existing VM hostname, hash table calculates same index
    #and simply overwrites the old IP address stored there.
    print(f"Network before IP update: {vm_network}")
    vm_network["Rhel-Web-02"] = "10.0.0.22"
    print(f"Network after updating Rhel-Web-02: {vm_network}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.
    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")
    #Deleting removes both hostname and IP address from map entirely
    print(f"Network before deletion: {vm_network}")
    del vm_network["Ubuntu-DesktopGUI"]
    print(f"Netowrk after decommisioning Ubuntu-DesktopGUI: {vm_network}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    # Demonstrate at least two edge cases.
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")
    #Edge case 1: Look up missing VM safely using .get()
    #Using .get() prevents program from crashing with a KeyError if VM is offline or doesnt exist
    missing_lookup = vm_network.get("Kali-Linux", "VM not found on network")
    print(f"Safe lookup for missing Kali-Linux: {missing_lookup}")

    #Edge case 2: safely deleting a missing VM
    #Attempting to 'del'a missing key crashes app, so we check if it exists in network first
    key_to_delete = "CentOS-OLD"
    if key_to_delete in vm_network:
        del vm_network[key_to_delete]
        print(f"Successfully deleted {key_to_delete}")
    else:
        print(f"Safe delete failed: {key_to_delete} does not exist to be removed")
if __name__ == "__main__":
    main()
