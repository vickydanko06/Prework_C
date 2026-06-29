#Creates header for my to-do list
print("=~"*40)
print(f"{'My To-Do List':^40}")
print("=~"*40)

#creates the beginning 3 tasks.
tasks = ["Buy groceries", "Finish homework", "Call the dentist"]

for i in range(len(tasks)):
    print(f"{i+1}. {tasks[i]}") #prints the tasks in a numbered list format

print("Total Tasks:", len(tasks)) #prints the total number of tasks in the list

update_list = input("What would you like to do? (1/2/3): \n1. Add a task\n2. Remove a task\n3. Exit program\n") #asks user if they want to add or remove a task from the list

if update_list == "1":
    add = input("Enter your new task: ")
    tasks.append(add) #adds the new task to the list
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}") #prints the tasks in a numbered list format
    print("Total Tasks:", len(tasks)) #prints the total number of tasks in the list
elif update_list == "2":
    remove = input("Enter the number of the task you would like to remove: ") #asks user which task they would like to remove
    try:
        tasks.pop(int(remove) - 1) #removes the task from the list
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}") #prints the tasks in a numbered list format
        print("Total Tasks:", len(tasks)) #prints the total number of tasks in the list
    except (ValueError):
        print("Invalid task number.")#handles a case where an invalid task exists
elif update_list == "3":
    print("Exiting program.")#exits program
else:
    print("Invalid input. Please enter '1', '2', or '3'.")#handles if a user inputs a wrong value from the original prompt



