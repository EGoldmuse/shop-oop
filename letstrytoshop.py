

def show_instructions():
    print("""Type 'add' to add a new item to your shopping cart.
Type 'quit' to exit the Market.
Type 'remove' to remove an item from your shopping cart.
Type 'show' to list all items in your shopping cart""")

class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
    def __repr__(self):
        return f'Item {self.name} ${self.price}'

def shopping_cart():
    input('Welcome to the Market! Press enter to continue ')
    
    done = False
    cart = []

    while not done:
        
        choice = input("What do you want to do? (add/remove/show/quit) ").lower()
        
        if choice == 'add':
            name = input("Type in the item you wish to purchase. ").title()
            price =  input("Type in the items price. ").title()
            amount = input('How many?')
            item = Product(name, price, amount)
            cart_dict.append(item)
            
            
            cart_dict = {
                'item': item
                
            }
            
            cart.append(cart_dict)
            
        elif choice == 'show':
            total=0
            for item in info:
                total+=(float(item.amount) * float(item.price))
                print(item)
            print('==============================\nShopping Cart Total:  $' + str(total))
            input('Press any key continue')

        elif choice == 'quit':
            for item in info:
                print(item)
            confirm = input('Are are you sure you want to quit? Y/N? ').lower()
            if confirm == 'y':
                total=0
                for item in info:
                    total+=(float(item.amount) * float(item.price))
                    print(item)
                print('==============================\nShopping Cart Total:  $' + str(total))
                done = True
            elif confirm == 'n':
                    continue

        elif choice == 'remove':
            removed = input('Type in the name of item to be removed. ').title()
            cart_dict.pop()
    
        else:
            print("That's not a valid option, please choose something else.")
    
shopping_cart()