# Python Function and Scope Example

This Python script demonstrates the usage of function scope, `nonlocal` keyword, and arithmetic operations.

## Code Description:

### 1. Code Structure:

- **User Input for List:**
  - The program prompts the user to enter the number of elements required in a list.
  - User input is taken to form the list.

- **Function `func`:**
  - Defines a function named `func`.
  - Inside `func`:
    - Initializes `var1` with the value 3.
    - Prints the value of `var1`.
    - Defines another function `funct2` inside `func`.
      - Uses the `nonlocal` keyword to modify the outer `var1` within the nested function.
      - Changes the value of `var1` to 4.
      - Prints the updated value of `var1`.
    - Calls `funct2`.
    - Prints the value of `var1` again.
  - Calls `func` from the main part of the script.
  - Prints the value of `var1` after the function call.

- **Output:**
  - The script outputs the values of `var1` at different points in the program's execution.

### 2. Function Execution:

- **Scope of Variables:**
  - Demonstrates the concept of variable scope within functions.
  - Shows the use of `nonlocal` to modify a variable in an outer scope from a nested function.

### 3. Arithmetic Operations:

- **Arithmetic Operations Example:**
  - Arithmetic operations such as square, cube, and square root are not explicitly mentioned in the code but can be implemented using the variables `var1` and other values.

### 4. Stack Frame and Function Call:

- **Function Call and Stack Frame:**
  - Illustrates how function calls create and manage stack frames.
  - Changes to variable values within a function do not affect the outer scope unless specified with `nonlocal` or `global` keywords.
