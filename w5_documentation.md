# Week 5 Tutorial 5

## 1. Answer Below Questions

### 1.1 Define the Problem Statement

The problem is that the cashier calculates the customer bill manually. This can waste time and the cashier may make mistakes.

So, I need to create a simple Python program that asks for the customer's name and the quantity of coffee, tea, and sandwich. Then the program will calculate the total bill and print a receipt.

### 1.2 What Are the Inputs?

The inputs are:

- Customer name
- Coffee quantity
- Tea quantity
- Sandwich quantity

### 1.3 What Are the Outputs?

The outputs are:

- Customer name
- Coffee quantity
- Tea quantity
- Sandwich quantity
- Total price in RM
- Receipt

### 1.4 What Would Be the Typical Process Flow?

The typical process is:

1. Start the program.
2. Enter customer name.
3. Enter coffee quantity.
4. Enter tea quantity.
5. Enter sandwich quantity.
6. Calculate the total price.
7. Print the receipt.
8. End the program.

### 1.5 What Are the Constraints?

The constraints are:

- Coffee price is RM 8.50.
- Tea price is RM 6.00.
- Sandwich price is RM 12.00.
- Quantity must be a whole number.
- Quantity cannot be negative.
- Customer name cannot be empty.
- Total must be shown with two decimal places.

## 2. How Do You Decompose the Problem Into Smaller Tasks?

I can break the problem into small tasks:

1. Store the price for each item.
2. Ask the user to enter customer name.
3. Ask the user to enter the quantity for each item.
4. Check that the quantity is valid.
5. Multiply each quantity by its price.
6. Add all prices to get the total.
7. Print the receipt.

This helps me understand the program better because I can solve one small part at a time.

## 3. Pseudocode

```text
START

SET coffee_price = 8.50
SET tea_price = 6.00
SET sandwich_price = 12.00

ASK user for customer name
ASK user for coffee quantity
ASK user for tea quantity
ASK user for sandwich quantity

CALCULATE total:
total = (coffee quantity * coffee price)
      + (tea quantity * tea price)
      + (sandwich quantity * sandwich price)

PRINT receipt
PRINT customer name
PRINT coffee quantity
PRINT tea quantity
PRINT sandwich quantity
PRINT total

END
```

## 4. Write the Code

### 4.1 Logic Functions From `utils.py`

I put the calculation function in `utils.py` because it is easier to manage the code.

```python
def calculate_total(coffee, tea, sandwich):
    coffee_total = coffee * 8.50
    tea_total = tea * 6.00
    sandwich_total = sandwich * 12.00
    total = coffee_total + tea_total + sandwich_total
    return total
```

I also put the receipt function in `utils.py`.

```python
def print_receipt(customer_name, coffee, tea, sandwich, total):
    print("\n===== RECEIPT =====")
    print(f"Customer : {customer_name}")
    print(f"Coffee   : {coffee}")
    print(f"Tea      : {tea}")
    print(f"Sandwich : {sandwich}")
    print("-------------------")
    print(f"Total = RM {total:.2f}")
```

### 4.2 Main Program From `main.py`

The main program asks the user for input, calls the calculation function, and prints the receipt.

```python
customer_name = get_customer_name()
coffee = get_quantity("Coffee")
tea = get_quantity("Tea")
sandwich = get_quantity("Sandwich")

total = calculate_total(coffee, tea, sandwich)
print_receipt(customer_name, coffee, tea, sandwich, total)
```

## Sample Input

```text
Customer name: Bobby
Coffee quantity: 3
Tea quantity: 3
Sandwich quantity: 2
```

## Sample Output

```text
===== RECEIPT =====
Customer : Bobby
Coffee   : 3
Tea      : 3
Sandwich : 2
-------------------
Total = RM 67.50
```

## What I Learned

From this tutorial, I learned how to:

- Use functions in Python.
- Separate the main program and utility functions.
- Get input from the user.
- Calculate a total using variables.
- Print a simple receipt.
- Check invalid input so the program does not crash.
