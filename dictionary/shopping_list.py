shopping_items = {
    "1": "computer",
    "2": "smartphone",
    "3": "keyboard",
    "4": "power bank",
    "5": "mouse"
}

price_quantity = {
    "computer": {"price": 500, "quantity": 10},
    "smartphone": {"price": 1000, "quantity": 3},
    "keyboard": {"price": 25, "quantity": 8},
    "power bank": {"price": 15, "quantity": 4},
    "mouse": {"price": 10, "quantity": 5},
}
total_price = 0
print("Enter the digit to add item to shopping list \n 1: computer\n 2: smartPhone\n\
    3: keyboard\n 4: power bank\n 5: mouse\n 0: stop shopping")
key_list = []
while True:
    user_input = input("\t")
    if user_input == "0":
        break
    else:
        for keys, values in shopping_items.items():
            key_list.append(keys)
            if user_input not in key_list:
                print("out of bounds")
            if user_input == keys:
                print(f"Adding {values}")
                price = int(price_quantity[values]["price"])
                quantity = int(price_quantity[values]["quantity"])
                total_price = total_price + price
                quantity = quantity - 1
                if quantity == 0:
                    print(f"{values} is out of stock")
print(f"Total price is ${total_price}")