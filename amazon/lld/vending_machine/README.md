Requirement:
1. Vending machine should support various products with its own quantities and prices
2. Vending machine should accept coin for the payment
3. Vending machine should dispense the selected product and return change if any
4. Vending machine should always keep track of product availability
5. Vending machine should able to handle insufficient money and product not available case
6. Vending machine should have different states where in each state, there're several capabilities that it can't do / can do

Class:
1. Vending Machine
    a. Products
2. Product
    a. Price
    b. Quantity

Design Pattern:
1. Singleton : when create the vending machine object and its states, so to ensure we reuse the same object instead of creating new one
2. State