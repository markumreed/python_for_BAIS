---
jupyter: python3
---

## Introduction to Python Programming Basics for Business

Python is a versatile, high-level programming language known for its readability and broad applicability, especially in the business world. This tutorial will introduce you to the fundamentals of Python, focusing on business-related examples. You will learn about variables, data types, control structures, functions, and basic modules.

### Variables and Data Types

#### Variables

In Python, variables are used to store data values. You do not need to declare a variable before using it.

```{python}
# Example
company_name = "Tech Solutions Inc."
number_of_employees = 250
is_public = True
```

#### Data Types

1. **Strings**: A sequence of characters.
    ```{python}
    greeting = "Welcome to our company!"
    ```
2. **Integers**: Whole numbers.
    ```{python}
    total_sales = 150000
    ```
3. **Floats**: Decimal numbers.
    ```{python}
    quarterly_profit = 35000.75
    ```
4. **Booleans**: True or False values.
    ```{python}
    is_profit_increasing = False
    ```

### Basic Operations

Python supports various operations on data types.

#### Arithmetic Operations

```{python}
revenue = 100000
expenses = 75000

net_income = revenue - expenses  # Subtraction
print(net_income)  # Output: 25000

profit_margin = (net_income / revenue) * 100  # Division
print(profit_margin)  # Output: 25.0
```

#### String Operations

```{python}
department1 = "Finance"
department2 = "Marketing"

# Concatenation
combined_departments = department1 + " and " + department2
print(combined_departments)  # Output: Finance and Marketing

# Length
department_length = len(department1)
print(department_length)  # Output: 7
```

### Control Structures

#### Conditional Statements

Conditional statements allow you to execute code based on conditions.

```{python}
annual_revenue = 1200000

if annual_revenue > 1000000:
    print("The company qualifies for the large enterprise category.")
else:
    print("The company qualifies for the small enterprise category.")
```

#### Loops

Loops are used to iterate over a sequence of elements.

##### For Loop

```{python}
departments = ["Finance", "Marketing", "HR", "IT"]

for department in departments:
    print(department)
```

##### While Loop

```{python}
pending_tasks = 5

while pending_tasks > 0:
    print(f"Tasks remaining: {pending_tasks}")
    pending_tasks -= 1
```

### Functions

Functions are blocks of code that perform a specific task and can be reused.

#### Defining and Calling Functions

```{python}
def calculate_bonus(salary, performance_rating):
    bonus_percentage = 0.1 if performance_rating >= 4 else 0.05
    return salary * bonus_percentage

print(calculate_bonus(50000, 4.5))  # Output: 5000.0
```

#### Functions with Multiple Arguments

```{python}
def calculate_total_cost(unit_price, quantity):
    return unit_price * quantity

print(calculate_total_cost(50, 100))  # Output: 5000
```

### Lists

Lists are ordered collections of items.

#### Creating and Accessing Lists

```{python}
clients = ["Client A", "Client B", "Client C"]

print(clients[0])  # Accessing first element, Output: Client A
print(clients[-1]) # Accessing last element, Output: Client C
```

#### Adding and Removing Elements

```{python}
clients.append("Client D")  # Adding an element
clients.remove("Client B")  # Removing an element
print(clients)  # Output: ['Client A', 'Client C', 'Client D']
```

### Dictionaries

Dictionaries store data in key-value pairs.

#### Creating and Accessing Dictionaries

```{python}
employee = {
    "name": "John Doe",
    "age": 30,
    "position": "Data Analyst"
}

print(employee["name"])  # Accessing value by key, Output: John Doe
```

#### Adding and Removing Key-Value Pairs

```{python}
employee["salary"] = 70000  # Adding a new key-value pair
del employee["age"]         # Removing a key-value pair
print(employee)  # Output: {'name': 'John Doe', 'position': 'Data Analyst', 'salary': 70000}
```

### Basic Modules and Importing

Python has a rich standard library of modules you can import to extend functionality.

#### Importing Modules

```{python}
import math

# Calculating the ceiling value of monthly earnings
monthly_earnings = 10234.56
print(math.ceil(monthly_earnings))  # Output: 10235
```

#### Importing Specific Functions

```{python}
from math import sqrt

# Calculating the square root of the annual growth percentage
annual_growth = 16
print(sqrt(annual_growth))  # Output: 4.0
```

### Conclusion

This tutorial covered the basics of Python programming with a focus on business-related examples, including variables, data types, control structures, functions, lists, dictionaries, and basic module usage. With these fundamentals, you can start building simple Python programs to solve business problems and gradually move on to more complex projects.

# Deep Dive Tutorial into Python Basics

Python is a high-level, interpreted programming language known for its readability, simplicity, and versatility. It is widely used for web development, data analysis, artificial intelligence, scientific computing, and more. This tutorial provides a comprehensive introduction to the basics of Python, covering essential concepts and practical examples.

## Table of Contents

1. [Introduction to Python](#introduction-to-python)
2. [Installing Python](#installing-python)
3. [Running Python Programs](#running-python-programs)
4. [Python Syntax and Semantics](#python-syntax-and-semantics)
    - [Indentation](#indentation)
    - [Comments](#comments)
5. [Variables and Data Types](#variables-and-data-types)
    - [Numbers](#numbers)
    - [Strings](#strings)
    - [Booleans](#booleans)
    - [None](#none)
6. [Operators](#operators)
    - [Arithmetic Operators](#arithmetic-operators)
    - [Comparison Operators](#comparison-operators)
    - [Logical Operators](#logical-operators)
    - [Assignment Operators](#assignment-operators)
    - [Membership Operators](#membership-operators)
    - [Identity Operators](#identity-operators)
7. [Control Flow](#control-flow)
    - [Conditional Statements](#conditional-statements)
    - [Loops](#loops)
8. [Functions](#functions)
    - [Defining Functions](#defining-functions)
    - [Function Arguments](#function-arguments)
    - [Return Values](#return-values)
9. [Data Structures](#data-structures)
    - [Lists](#lists)
    - [Tuples](#tuples)
    - [Sets](#sets)
    - [Dictionaries](#dictionaries)
10. [Modules and Packages](#modules-and-packages)
    - [Importing Modules](#importing-modules)
    - [Creating Modules](#creating-modules)
    - [Using Packages](#using-packages)
11. [File Handling](#file-handling)
    - [Reading Files](#reading-files)
    - [Writing Files](#writing-files)
12. [Exception Handling](#exception-handling)
13. [Conclusion](#conclusion)

## Introduction to Python

Python was created by Guido van Rossum and first released in 1991. It emphasizes code readability and allows programmers to express concepts in fewer lines of code than languages like C++ or Java. Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

## Installing Python

To install Python, download the installer from the [official Python website](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

## Running Python Programs

Python programs can be run in various ways:
- **Interactive Mode**: Open a terminal or command prompt, type `python` or `python3`, and press Enter.
- **Script Mode**: Write your code in a file with a `.py` extension and run it using `python filename.py` or `python3 filename.py`.

## Python Syntax and Semantics

### Indentation

Python uses indentation to define the structure of the code. Consistent indentation is crucial as it defines blocks of code.

```{python}
if 5 > 2:
    print("Five is greater than two!")
```

### Comments

Comments are used to explain code and are ignored by the interpreter. Single-line comments start with `#`.

```{python}
# This is a comment
print("Hello, World!")  # This is an inline comment
```

## Variables and Data Types

Variables are used to store data values. In Python, you don't need to declare variables before using them.

```{python}
x = 5
y = "Hello"
```

### Numbers

Python supports integers, floating-point numbers, and complex numbers.

```{python}
a = 10       # Integer
b = 3.14     # Float
c = 1 + 2j   # Complex
```

### Strings

Strings are sequences of characters enclosed in single, double, or triple quotes.

```{python}
name = "Alice"
greeting = 'Hello, World!'
multiline = """This is
a multiline
string."""
```

### Booleans

Booleans represent `True` or `False`.

```{python}
is_true = True
is_false = False
```

### None

`None` represents the absence of a value.

```{python}
nothing = None
```

## Operators

### Arithmetic Operators

```{python}
x = 10
y = 3
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y) # Exponentiation
print(x // y) # Floor Division
```

### Comparison Operators

```{python}
print(x == y)  # Equal
print(x != y)  # Not equal
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to
```

### Logical Operators

```{python}
print(x > 5 and y < 5)  # Logical AND
print(x > 5 or y > 5)   # Logical OR
print(not(x > 5))       # Logical NOT
```

### Assignment Operators

```{python}
x = 10
x += 5  # x = x + 5
x -= 3  # x = x - 3
x *= 2  # x = x * 2
x /= 2  # x = x / 2
x %= 3  # x = x % 3
x **= 2 # x = x ** 2
x //= 2 # x = x // 2
```

### Membership Operators

```{python}
lst = [1, 2, 3, 4, 5]
print(3 in lst)  # True
print(6 in lst)  # False
print(6 not in lst)  # True
```

### Identity Operators

```{python}
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)      # False (different objects)
print(a is not b)  # True
print(a == b)      # True (same content)
```

## Control Flow

### Conditional Statements

```{python}
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
```

### Loops

#### `for` Loop

```{python}
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

#### `while` Loop

```{python}
i = 1
while i < 6:
    print(i)
    i += 1
```

#### Loop Control Statements

```{python}
for i in range(10):
    if i == 5:
        break  # Exit the loop
    if i % 2 == 0:
        continue  # Skip the rest of the loop
    print(i)
```

## Functions

### Defining Functions

```{python}
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
```

### Function Arguments

```{python}
def add(a, b):
    return a + b

print(add(3, 5))  # Positional arguments
print(add(a=3, b=5))  # Keyword arguments

def greet(name, message="Hello"):
    print(f"{message}, {name}!")
greet("Alice")
greet("Bob", "Hi")
```

### Return Values

```{python}
def square(x):
    return x * x

result = square(4)
print(result)
```

## Data Structures

### Lists

```{python}
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Accessing elements
fruits[1] = "blackberry"  # Modifying elements
print(fruits)
fruits.append("orange")  # Adding elements
print(fruits)
```

### Tuples

```{python}
coordinates = (10, 20)
print(coordinates[0])
# coordinates[0] = 30  # Error: Tuples are immutable
```

### Sets

```{python}
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # {1, 2, 3, 4}
unique_numbers.add(5)
print(unique_numbers)
```

### Dictionaries

```{python}
person = {"name": "Alice", "age": 30}
print(person["name"])
person["age"] = 31
print(person)
person["city"] = "New York"
print(person)
```

## Modules and Packages

### Importing Modules

```{python}
import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(16))
```

### Creating Modules

Create a file named `mymodule.py`:

```{python}
# mymodule.py
def greet(name):
    print(f"Hello, {name}!")
```

Then import and use it:

```{python}
import mymodule
mymodule.greet("Alice")
```

### Using Packages

Create a package directory structure:

```
mypackage/
    __init__.py
    module1.py
    module2.py
```

In `module1.py`:

```python
def function1():
    print("Function 1 from module 1")
```

In `module2.py`:

```python
def function2():
    print("Function 2 from module 2")
```

In `__init__.py`:

```python
from .module1 import function1
from .module2 import function2
```

Then use the package:

```{python}
import mypackage
mypackage.function1()
mypackage.function2()
```

## File Handling

### Reading Files

```{python}
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Writing Files

```{python}
with open('file.txt', 'w') as file:
    file.write("Hello, World!")
```

## Exception Handling

```{python}
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This is always executed")
```

## Conclusion

This deep dive tutorial covered the basics of Python, including syntax, data types, operators, control flow, functions, data structures, modules, file handling, and exception handling. By mastering these fundamentals, you'll be well-equipped to explore more advanced topics and develop robust Python applications. Python's simplicity and readability make it an excellent choice for beginners and experienced developers alike.