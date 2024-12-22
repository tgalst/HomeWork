apple = 0
choco = 0
apple_price = 1
choco_price = 3
print("0 - Exit")
print("1 - Repeat this message")
print("2 - Add one apple to cart (apple price is 1$)")
print("3 - Remove one apple from cart")
print("4 - Add one chocolate to cart (chocolate price is 3$)")
print("5 - Remove one chocolate from cart")
print("6 - Show my cart")
print("7 - Show checkout information")
while True:
    print()
    action = input("What to do? ")
    if action == '0':
        print("Exit from shop")
        break
    elif action == '1':
        print("0 - Exit")
        print("1 - Repeat this message")
        print("2 - Add one apple to cart (apple price is 1$)")
        print("3 - Remove one apple from cart")
        print("4 - Add one chocolate to cart (chocolate price is 3$)")
        print("5 - Remove one chocolate from cart")
        print("6 - Show my cart")
        print("7 - Show checkout information")
        continue
    elif action == '2':
        apple = apple + 1
        print("Added apple in the cart:", apple)
    elif action == '3':
        apple = apple - 1
        if apple < 0:
            apple = 0
        print("Removed apple from the cart:", apple)
    elif action == '4':
        choco = choco + 1
        print("Added choco in the cart:", choco)
    elif action == '5':
        choco = choco - 1
        if choco < 0:
            choco = 0
        print("Removed apple from the cart:", choco)
    elif action == '6':
        print("apple = ", apple, "choco = ", choco)
    elif action == '7':
        apple_total = apple * apple_price
        choco_total = choco * choco_price
        print(f"apple = {apple} - {apple_total}$")
        print(f"choco = {choco} - {choco_total}$")
        print("__________________________________")
        print(f"Total: {apple_total + choco_total}$")
        break
    else:
        print("Wrong input, please try again")