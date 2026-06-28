print("=~" *3 + " Road Trip Budget Planner " + "=~" *3) #header formatting for the trip_planner

#All user prompts:
#get destination from user
destination = input("Where are you going? ")
#get total distance in miles from user
distance = float(input("What is the total distance of your trip in miles? "))
#get fuel efficiency in miles per gallon
efficiency = float(input("What is your vehicle's fuel efficiency in miles per gallon? "))
#get price of gas per gallon
gas_price = float(input("What is the price of gas per gallon? "))
#get number of nights user will stay
nights = int(input("How many nights will you be staying? "))
#get average cost of hotel per night
hotel_cost = float(input("What is the average cost of a hotel per night? "))
#get cost of daily food budget
food_budget = float(input("What is your daily food budget? "))  

#All calucations are below:
#gas needed calculated below
gas_needed = distance / efficiency
#total gas cost calculated below
total_gas_cost = gas_needed * gas_price
#total hotel cost calculated below
total_hotel_cost = nights * hotel_cost
#total food cost calculated below
total_food_cost = (nights+1) * food_budget
#total trip cost calculated below
total_trip_cost = total_gas_cost + total_hotel_cost + total_food_cost

#Formatting for the output of the trip_planner file
print(f"\nDestination: {destination}") #prints the destination
print(f"Distance: {distance} miles")#prints the total distance
print(f"_____" + "Cost Breakdown: " + "_____")#prints header for the breakdown of costs
print(f"Gas Cost: ${total_gas_cost:.2f}" + f" ({gas_needed:.2f} gal @ ${gas_price}/gal)")#prints the total gas cost
print(f"Hotel Cost: ${total_hotel_cost:.2f}" + f" ({nights} nights @ ${hotel_cost}/night)")#prints the total hotel cost
print(f"Food Cost: ${total_food_cost:.2f}" + f" ({nights+1} days @ ${food_budget}/day)")#prints the total food cost
print("_"*40)
print(f"Estimated Trip Total: ${total_trip_cost:.2f}")#prints the total


