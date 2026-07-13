import csv

#read sales data from a CSV file
sales_data = []

with open('sales_data.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # convert quantity and price to numeric types
        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])
        sales_data.append(row)

print(f"Sales Data Loaded: {len(sales_data)} records")

#Calculations for sales data total revenue
total_revenue = sum(row["quantity"] * row["price"] for row in sales_data)
print(f"Total Revenue: ${total_revenue:.2f}")
# Revenue per product
revenue_per_product = {}

# Total quantity sold per product
quantity_per_product = {}

revenue_per_day = {}

for row in sales_data:
    product = row["product"]
    quantity = row["quantity"]
    revenue = quantity * row["price"]

    
    # Revenue per product
    revenue_per_product[product] = (
        revenue_per_product.get(product, 0) + revenue
    )

    # Quantity per product
    quantity_per_product[product] = (
        quantity_per_product.get(product, 0) + quantity
    )

    date = row["date"].strip()

revenue_per_day[date] = revenue_per_day.get(date, 0) + revenue

# Write results to a text file
all_items = [p["product"] for p in sales_data]

with open("sales_report.txt", "w") as file:
    file.write("SALES REPORT\n")
    file.write("=" * 40 + "\n")
    file.write(f"Total revenue: ${total_revenue:.2f}\n")
    file.write("\nRevenue per product:\n")
    for product, revenue in revenue_per_product.items():
        file.write(f"  {product}: ${revenue:.2f}\n")
    file.write("\nQuantity sold per product:\n")
    for product, quantity in quantity_per_product.items():
        file.write(f"  {product}: {quantity}\n")
    file.write(f"\nDay with the highest total revenue:\n")
    
    highest_revenue_date = max(revenue_per_day, key=revenue_per_day.get) 
    file.write(f"  {highest_revenue_date}: ${revenue_per_day[highest_revenue_date]:.2f}\n")
print("\nReport written to sales_report.txt")

#Writes process data to a new csv
with open("product_summary.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["product", "total_quantity", "total_revenue"])
    writer.writeheader() 

    for product in quantity_per_product:
        writer.writerow({
            "product": product,
            "total_quantity": quantity_per_product[product],
            "total_revenue": f"{revenue_per_product[product]:.2f}"
        })
       

print("Product summary data written to product_summary.csv")
