"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================
STUDENT NAME: DIMITRIOS KAKOULLIS

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.# Requirements:
# # - Include at least one class variable.
# # - Include at least two instance variables.
# # - Include a constructor (__init__).
# # - Include a method that returns or displays information about the object.
# #
# # Replace the pass statement with your implementation.
class ComputerComponent:
    #class shared by all instances
    category = "PC Hardware"
    def __init__(self, manufacturer, model):
        #instance variable that will be unique to each object
        self.manufacturer = manufacturer
        self.model = model

    def display_specs(self):
        return f"Component: {self.manufacturer}{self.model}"




# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.  done
# - Add at least two new instance variables.  done
# - Add at least one new method.  done
# - Override a method from the parent class.  done
#
# Replace the pass statement with your implementation.

class GraphicsCard(ComputerComponent):
    #new class variable that will inherit from parent class
    component_type = "GPU"

    def __init__(self, manufacturer, model, vram_gb, supported_resolutions):
        super().__init__(manufacturer, model)

        #new instance variables
        self.vram_gb = vram_gb
        self.supported_resolutions = supported_resolutions

    #override method from parent class
    def display_specs(self):
        base_specs = super().display_specs()
        return f"{base_specs} | VRAM: {self.vram_gb}GB | Type: {self.component_type}"
    #new method specific to child class
    def add_resolution(self, resolution):
        if resolution not in self.supported_resolutions:
            self.supported_resolutions.append(resolution)
            return f"Added {resolution} display support."
        return "Resolution already supported!"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself. done
# - Access the same class variable through an object.  done
# - Add a new attribute to only one object after it is created. done
# - Display each object's namespace using __dict__.  done
# - Display information about the class namespace.   done

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    #- Create at least two objects of the child class.
    gpu1 = GraphicsCard("EVGA", "GeForce RTX 2070 Super", 8, ["1080p", "1440p", "4K"])
    gpu2 = GraphicsCard("Nvidia", "RTX 4090", 24, ["1440p", "4k", "8K"])

    # Access a class variable through the class itself AND access same class variable throuh object
    print("Class variable through class itself:", GraphicsCard.component_type)
    print("Class variable through object:", gpu1.component_type)

    # - Add a new attribute to only one object after it is created.
    gpu1.overclocked = True

    # - Display each object's namespace using __dict__.
    print("\nGPU 1 Namespace:", gpu1.__dict__)
    print("GPU 2 Namespace:", gpu2.__dict__)

    # - Display information about the class namespace.
    clean_class_dict = {k: v for k, v in GraphicsCard.__dict__.items() if not k.startswith('__')}
    print("Child Class Namespace:", clean_class_dict)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    # - Create an object that contains nested mutable data.
    original_gpu = GraphicsCard("EVGA", "GeForce RTX 2070 Super", 8, ["1080p", "1440p"])

    #create a shallow and deep copy of each
    shallow_gpu = copy(original_gpu)
    deep_gpu = deepcopy(original_gpu)

    #modify orignal nested data from object
    original_gpu.supported_resolutions.append("4K")

    #A shallow copy can only duplicate top-level objects but does actually point to same NESTED list in memory.
    #If original list is changed, the shallow copy will also change.
    #Deep copy means every bit of information is copied recursively, meaning the nested list created in memory
    #exist independently and unaffected by any change made to original object

    print("Original Resolutions:", original_gpu.supported_resolutions)
    print("Shallow Copy Resolutions:", shallow_gpu.supported_resolutions)
    print("Deep Copy Resolutions:", deep_gpu.supported_resolutions)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    cpu = ComputerComponent("AMD", "Ryzen 9")
    print(cpu.display_specs())

    print("\nTODO: Create and test your child object")
    gpu = GraphicsCard("EVGA", "Geforce RTX 2070 Super", 8, ["1080p", "1440p"])
    print(gpu.display_specs())
    print(gpu.add_resolution("4K"))

    #call copy and namespace function
    demonstrate_namespaces()
    demonstrate_copying()



if __name__ == "__main__":
    main()