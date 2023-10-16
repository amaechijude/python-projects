shopping_items = {
    "1": "computer",
    "2": "smartphone",
    "3": "keyboard",
    "4": "power bank",
    "5": "mouse",
    "6": "usb-c",
    "7": "hdmi",
    "8": "monitor",
    "9": "flash drive"
}

price_quantity = {
    "computer": {"price": 500, "quantity": 10},
    "smartphone": {"price": 1000, "quantity": 3},
    "keyboard": {"price": 25, "quantity": 8},
    "power bank": {"price": 15, "quantity": 4},
    "mouse": {"price": 10, "quantity": 5},
    "usb-c": {"price": 3, "quantity": 0},
    "hdmi": {"price": 4, "quantity": 20},
    "monitor": {"price": 300, "quantity": 1},
    "flash drive": {"price": 3, "quantity": 2}
}
#Display items and request input
print("Enter number to add items to shopping list")
for keys, values in shopping_items.items():
    print(f"{keys}: {values}")
print("0: end/checkout")


user_input = input(">> ")
total_price = 0

#check if the item is available in the list
while user_input != "0":
    if user_input in shopping_items:
        #logic
        current_choice = shopping_items[user_input]
        if price_quantity[current_choice]["quantity"] > 0:
            print(f"Adding {current_choice}")
            price_quantity[current_choice]["quantity"] -= 1
            total_price += price_quantity[current_choice]["price"]
        else:
            print(f"{current_choice} is out of stock")

    else:
        print("Item is not available")

    user_input = input(">> ")
print(f"Total price is ${total_price}")