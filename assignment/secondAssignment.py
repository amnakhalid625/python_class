# Task 1: Student Marks Analyzer
# Create a dictionary containing student names and their marks. Use a loop to print
# each student’s name and assign a grade based on their marks using if-elif-else.


students = {
    "Ali": 85,
    "Ayesha": 72,
    "Zain": 58,
    "Sara": 91,
    "Bilal": 40
}

for name, marks in students.items():
    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"
    
    print(f"{name} got {marks} marks and their grade is {grade}")



# Task 2: Shopping Cart Manager
# Create a list of items where each item has a name and a price. Ask the user for their
# budget and use a loop with if-else to check which items they can afford.

items = [
    {"name": "Shoes", "price": 2000},
    {"name": "Bag", "price": 1500},
    {"name": "Watch", "price": 3000},
    {"name": "Perfume", "price": 1000}
]

budget = int(input("Enter your budget: "))

print("\nYou can afford the following items:")

for item in items:
    if item["price"] <= budget:
        print(f"- {item['name']} (Rs {item['price']})")
    else:
        print(f"- {item['name']} is too expensive for your budget.")



# Task 3: Inventory Quantity Checker
# Make a dictionary of items and their quantities. Use a for loop and if-else to print
# whether each item is &quot;In Stock&quot; or &quot;Out of Stock&quot; based on its quantity.


inventory = {
    "Pens": 10,
    "Notebooks": 0,
    "Markers": 5,
    "Erasers": 0,
    "Folders": 3
}

for item, quantity in inventory.items():
    if quantity > 0:
        print(f"{item}: In Stock")
    else:
        print(f"{item}: Out of Stock")


# Task 4: Class Result Summary
# Create a list of dictionaries, each containing a student&#39;s name and their marks in 3
# subjects. Use a loop to calculate the average and use if-else to display whether the
# student has passed or failed.


# List of students with marks in 3 subjects
students = [
    {"name": "Ali", "math": 70, "english": 65, "science": 80},
    {"name": "Sara", "math": 40, "english": 45, "science": 38},
    {"name": "Zain", "math": 85, "english": 75, "science": 90},
    {"name": "Ayesha", "math": 55, "english": 60, "science": 58}
]

for student in students:
    total = student["math"] + student["english"] + student["science"]
    average = total / 3

    if average >= 50:
        result = "Passed"
    else:
        result = "Failed"

    print(f"{student['name']} - Average: {average:.2f} - {result}")



#     Task 5: Item Search in Store
# Make a tuple of available items. Ask the user to input 3 item names (store them in a
# list), and use a for loop with if-else to check if each item is available in the store.


available_items = ("Pens", "Notebooks", "Markers", "Erasers", "Folders")

user_items = []

for i in range(3):
    item = input(f"Enter item {i + 1}: ")
    user_items.append(item)

for item in user_items:
    if item in available_items:
        print(f"{item} is available in the store.")
    else:
        print(f"{item} is not available in the store.")
        
