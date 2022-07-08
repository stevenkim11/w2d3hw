shopping_cart =[]
while True:
    user_input = input('Please type: Show/Add/Remove/Quit: ')
    if user_input == 'Add':
        item = input("Add item to cart: ")
        shopping_cart.append(item)
    elif user_input == "Quit":
        break
    elif user_input == "Show":
        print(shopping_cart)
    elif user_input == "Remove":
        removed = input("What would you like to remove? ")
        shopping_cart.remove(removed)

print(shopping_cart)
        