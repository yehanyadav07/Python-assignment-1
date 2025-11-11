# -----------------------------------------------------------
# Name:yehan yadav
# Date: 5 november 2025
# Project Title: Daily Calorie Tracker CLI
# -----------------------------------------------------------

import datetime

print("Welcome to the Daily Calorie Tracker")
print("This program helps you to track your daily calorie intake.\n")

# Task 2: Input and Data Collection
meals = []
calories = []

num_meals = int(input("Enter how many meals you had today: "))

for i in range(num_meals):
    print("\nMeal", i + 1)
    meal_name = input("Enter meal name (for example Breakfast, Lunch): ")
    calorie_amount = float(input("Enter calorie amount: "))
    meals.append(meal_name)
    calories.append(calorie_amount)

# Task 3: Calorie Calculations
total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    message = "You have exceeded your daily calorie limit."
else:
    message = "You are within your daily calorie limit."

# Task 5: Display Output
print("\n----------------------------------------")
print("           DAILY CALORIE REPORT          ")
print("----------------------------------------")
print("Meal Name\tCalories")
print("----------------------------------------")

for i in range(len(meals)):
    print(meals[i], "\t\t", calories[i])

print("----------------------------------------")
print("Total:\t\t", total_calories)
print("Average:\t", round(average_calories, 2))
print("----------------------------------------")
print(message)

# Task 6: Save Session Log to File (Bonus)
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()

if save == "yes" or save == "y":
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file = open("calorie_log.txt", "a")
    file.write("\n----------------------------------------\n")
    file.write("Session Time: " + time + "\n")
    file.write("----------------------------------------\n")
    file.write("Meal Name\tCalories\n")
    for i in range(len(meals)):
        file.write(meals[i] + "\t\t" + str(calories[i]) + "\n")
    file.write("----------------------------------------\n")
    file.write("Total: " + str(total_calories) + "\n")
    file.write("Average: " + str(round(average_calories, 2)) + "\n")
    file.write(message + "\n")
    file.write("----------------------------------------\n\n")
    file.close()
    print("Report saved to calorie_log.txt")
else:
    print("Report not saved.")

print("\nThank you for using the Daily Calorie Tracker.")
