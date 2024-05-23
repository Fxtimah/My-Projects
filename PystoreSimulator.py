def display_products(products):
    print("\nAvailable Products:")
    for key, value in products.items():
        print(f"{key}: ${value:.2f}")

def get_product_choice(products):
    while True:
        choice = input("\nEnter the product name you want to buy (or type 'q' to quit): ").strip()
        if choice.lower() == 'q':
            return None
        if choice in products:
            return choice
        else:
            print("Invalid product name. Please try again.")

def get_product_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    products = {
        "Laptop": 999.99,
        "Smartphone": 599.99,
        "Headphones": 199.99,
        "Charger": 49.99
    }

    cart = {}
    print("Welcome to the Online Store!")
    
    while True:
        display_products(products)
        choice = get_product_choice(products)
        if choice is None:
            break
        quantity = get_product_quantity()
        
        if choice in cart:
            cart[choice] += quantity
        else:
            cart[choice] = quantity

    if not cart:
        print("\nYou did not purchase any items.")
        return

    print("\nYour Shopping Cart:")
    total = 0
    for item, qty in cart.items():
        item_total = products[item] * qty
        print(f"{item} (x{qty}): ${item_total:.2f}")
        total += item_total

    print(f"\nTotal Amount: ${total:.2f}")
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()
