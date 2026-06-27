#items are all strings
item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"
item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"
item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"
tax_rate = "0.075"   # 7.5% sales tax

#converting price strings to price numbers as a float because it needs decimal points for the math calculations
price1 = float(item1_price)
price2 = float(item2_price)
price3 = float(item3_price)

#converting quantity strings to quantity numbers as an integer because you can only have a whole number of items
qty1 = int(item1_qty)
qty2 = int(item2_qty)
qty3 = int(item3_qty)

#converting tax rate string to tax rate number as a float because it needs decimal points for the math calculations
tax = float(tax_rate)

#Math calculations
line_total1 = price1 * qty1
line_total2 = price2 * qty2
line_total3 = price3 * qty3
subtotal = line_total1 + line_total2 + line_total3
tax_amount = subtotal * tax
total = subtotal + tax_amount

#Formatting of the receipt
print("=~"* 40)
print(f"Store Receipt")
print("=~"* 40)
print(f"{item1_name} ${item1_price} x {item1_qty} = ${line_total1:.2f}")
print(f"{item2_name} ${item2_price} x {item2_qty} = ${line_total2:.2f}")
print(f"{item3_name} ${item3_price} x {item3_qty} = ${line_total3:.2f}")
print("__"* 40)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax_amount:.2f}")
print("__"* 40)
print(f"Total: ${total:.2f}")
print("=~"* 40)
