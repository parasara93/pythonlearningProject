
# given any project in pytho we will  work on many modules
# here in this practice case multiple python files are multiple modules
# in a real time scenario it all the functions classes and methods might be in pne such module and are imported if needed
# to use one module in another we use the import keyword like import from module_name * or import from module_name function_name

# print("Demo says: ", __name__)
# the module we run first has the name main
# For the module that we are importing to this one the __name__ of it will be the name of the module
# when you work on a project everything should be a or mostly will be a function

# Example Scenario:
# For example there are 2 Module-1/Mod-1 and Module-2/Mod-2 where module-1 is being imported by module 2
# but, certain part of the code in module-1 is meant to execute only when executing module 1 but not while being imported by another module
# How would you achieve it below is one such example using just print statements

# Module-1
# Mod-1 file name is Modules.py

# To avoid Module-2 access this part of the code we first put it in function
def say_hi():
    print("hello")
    print("welcome user")
    print("this is the name of Mod-1 if executed first:", __name__)

if __name__ == "__main__":
    say_hi()
# so if the Module-1 is being imported then the name of the module-1 will not be main. it's name will be main if only it is executed first and not as a module

# the o/p of the below code will be more understandable when imported or executed in Mod-2
print("this is the name of Mod-1 if imported:", __name__)

# output of Mod-1
# hello
# welcome user
# this is the name of Mod-1 if executed first: __main__
# this is the name of Mod-1 if imported: __main__

# o/p of Mod-2
# this is the name of Mod-1 if imported: Modules
# time to calculate
# this is the name of Mod-2 if executed first: __main__

# coz of the if statement the function say_hi will only execute if the name is main and not when imported into another module as the name changes
