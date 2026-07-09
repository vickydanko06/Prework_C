import csv

#read sales data from a CSV file
sales_data = []

with open('sales_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # convert quantity and price to numeric types
        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])
        sales_data.append(row)

print(f"Sales Data Loaded: {len(sales_data)} records")

#Calculations for sales data
total_revenue = sum(row["quantity"] * row["price"] for row in sales_data)
revenue_per_product = 
total_quantity_sold_per_product = 
highest_total_revenue_date = 


