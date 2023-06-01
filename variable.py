# Single Variable
x = 5  # Assigning the value 5 to the variable x
print(x)  # Printing the value of x, which is 5

# Multiple Variables
a, b, c = 1, 2, 3  # Assigning the values 1, 2, and 3 to variables a, b, and c respectively
print(a, b, c)  # Printing the values of a, b, and c, which are 1, 2, and 3 respectively

# Global Variable
m = 5  # Assigning the value 5 to the global variable m

def hello():
    print(m)  # Accessing the global variable m and printing its value

hello()  # Calling the hello function, which will print the value of m
