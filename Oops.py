# Python support all types of programming
# Functional, Procedure and Object Oriented Programming
# Procedure - Modules level we might manipulate data
# Functional - we are not manipulating data but performing some operations on data like arithmatic operations
# Oops - Attributes - variables and behaviours - methods, in oops Functions are called as method
# class is the blueprint of a class

# Defining an example class
class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram_size = ram
        # __init__ is a special method like special variable __name__
        # To initialize the variables we use __init__
        # This will be called automatically for every object when you call a method
        # we are passing 3 arguments here comp1, cpu type and ram size
        # When an object has its own values we define intit to initialize or say assign those values as part of the class and method


    def config(self):
        print("the configuration is:", self.cpu, self.ram_size)

a = 5
print(type(a))
# in-built class

# Object Creation
# comp1 = Computer()
# Constructors - in the above line Computer() is called a constructor. A constructor gives the object of a given class
# comp1 is an object for the class Computer
# Above is an object without a variable
# An object can have multiple variables
# we define these variables in a constructor

comp1 = Computer('i5', 6)
comp2 = Computer('raizen', 9)
# we have computer with a cpu and ram
# we need to print it using class
# When computer-1/comp1 is an object it has 2 attributes one is cpu type and other is ram size
# In the same way computer-2/comp2 has 2 attributes with different values
# Now we need to print the cpu type and ram size of a given computer

print(type(comp1))
# user defined class

# how do we call a method
# config() - we can't call like this as it is in a class, we need access it with a class
# Also when we are calling a method we need to call it with an object or else it will throw a error

Computer.config(comp1)

# Alternate for calling a method, obj_name.method_name.()
comp1.config()
comp2.config()

# CONSTRUCTORS
# Every time we create an object it will take a dedicated space
# Size of an object depends on variable and number of variables
# A constructor allocates or decides on the amount of memory for an object
# Constructor calls the init method automatically

# SELF
# self represents the object for which we are calling the method
# for example in comp2.config() here config will run the method for object comp2 and its attributes
# i.e the function executes with the arguments of the object comp2 as its on arguments, to consider comp2 to we mention self


# to compare two objects we need to a method

# Types of Variables
# Instance variables and class variables
# Instance variables are the ones that are defined in the init method
# When you create variables out of init method and declare variables in class it is a class variable
class Cars:
    wheels = 4
    def __init__(self):
        self.milage = 8
        self.company = "BMW"

a = Cars()
b = Cars()
a.milage = 10
Cars.wheels = 12
print(a.milage, a.company, a.wheels)
print(b.milage, b.company, b.wheels)

# wheels is a class variable once you update class variable it applies to all the objects
# Where  as instance variables we need to update the value of a variable with an object we can update/change it class level
