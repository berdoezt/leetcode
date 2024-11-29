# 1. The user should be able to select
#    - size of the Pizza         Small, Medium, Large
#    - the type of base          thin, regular, cheesy crust
#    - the toppings              cheese, peperoni, bacon, mushrooms, olives, etc.
# Write a program that allows user to order and customize Pizza and calculate price.


// out of scope: payment, delivery
// requirement:
    1. the only product now is pizza, but can extend to other product
    2. displaying the price
        - the factor can be extend in the future
    3. (optional) can show in different currency

class Product: // parent
    size : enum(small, medium, large)
    price_properties : Price
    pass

class Price:
    pass

class PizzaPrice(Price):
    size: {
        "small": 100
        "medium": 200
        "large": 300
    }
    base : {
        "thin": 100
        "regular": 100
        "cheesy crust": 100
    },
    topping: {
        
        "cheese": 100,
        "peperoni": 200
    }
    

class Pizza(Product):
    base : enum(thin, regular, cheesy crust)
    topping : enum(cheese, peperoni, bacon)
    pass

class Pasta(Product):
    pass

class Order:
    id : string
    product: Product
    total_price: int // cent format
    pass
    
    def calculate_price():
        total_price = 0
        
        product.price_properties
            
        return total_price
        pass

class OrderManager:
    
    def get_products():
        //return all the products
        pass
    
    def create_order(product: Product):
        new Order(product)
        pass
    pass

 new Pizza(base, topping, size, PizzaPrice)
    