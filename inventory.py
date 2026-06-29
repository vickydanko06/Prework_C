inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "keyboard": {"price": 49.99, "quantity": 30},
    "monitor": {"price": 199.99, "quantity": 20},
}

#Calculations of the inventory list
laptop_total = inventory["laptop"]["price"] * inventory["laptop"]["quantity"]
mouse_total = inventory["mouse"]["price"] * inventory["mouse"]["quantity"]
keyboard_total = inventory["keyboard"]["price"] * inventory["keyboard"]["quantity"]
monitor_total = inventory["monitor"]["price"] * inventory["monitor"]["quantity"]
inventory_total = laptop_total + mouse_total + keyboard_total + monitor_total


#formatting of inventory list
print("=~"*40)
print(f"{'Inventory List':^40}")
print("=~"*40)

print(f"{'Name':<15}{'Price':<10}{'Quantity':<10}")
for name, details in inventory.items():
    print(f"{name:<15}${details['price']:<10.2f}{details['quantity']:<10}")

print("=~"*40)
print(f"{'Total Inventory Value:':<25}${inventory_total:.2f}")
print("=~"*40)

#allows user to search for an item in the inventory
search =input("Enter the name of the item to search: ").lower()
product = inventory.get(search)
if product:
    print(f"Item: {search.capitalize()}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Quantity: {product['quantity']}")
else:
    print(f"Item '{search}' not found in inventory.")

print("=~"*40)

#allows for a user to update the quantity of an item in the inventory
update_item = input("Enter the name of the item to update quantity: ").lower()
if update_item in inventory:
    new_quantity = int(input(f"Enter the new quantity for {update_item}: "))
    inventory[update_item]["quantity"] = new_quantity
    print(f"Quantity for {update_item} updated to {new_quantity}.")

else:
    print(f"Item '{update_item}' not found in inventory.")

#checks for low stock. if you change the original inventory to two items below 5 it takes into account for that as well. 
low_stock = set()
for name, info in inventory.items():
    if info["quantity"] < 10:
        low_stock.add(name)
        print(f"These products have low_stock: {name}")
              



