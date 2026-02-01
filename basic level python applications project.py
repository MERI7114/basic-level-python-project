print("HELLO WORLD")
print(input("MY NAME IS "))
print(input("MY AGE IS "))
print("WELCOME TO THE PROJECT")

 #EVEN OR ODD CHECKER  PROGRAM #
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# SIMPLE CALCULATOR  WITH USER CHOICE #

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Choose operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1/2/3/4): ")
if choice == "1":
    print("Result:", num1 + num2)
elif choice == "2":
    print("Result:", num1 - num2)
elif choice == "3":
    print("Result:", num1 * num2)
elif choice == "4":
    print("Result:", num1 / num2)
else:
    print("Invalid choice")

     #NUMBER GUSSING GAME PROGRAM #

import random
secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == secret_number:
    print(" Congratulations! You guessed it right.")
else:
    print(" Wrong guess.")
    print("The correct number was:", secret_number)


 # AGE CALCULATOR PROGRAM #

current_year = 2026
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print("Your age is:", age)


  # MULTIPLICATION TABLE GENERATOR  PROGRAM #
  
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

    # SIMPLE LOGIN SYSTEM  PROJECT #
correct_username = "admin"
correct_password = "1234"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_username and password == correct_password:
    print("Login Successful ")
else:
    print("Invalid Username or Password ")

# STUDENT GRADE CALCULATOR PROGRAM #

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")

#  SIMPLE TO-DO LIST APP  PROGRAM #



tasks = []   
while True:
    print("\n--- TO DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("✅ Task added successfully")
    elif choice == "2":
        if len(tasks) == 0:
            print(" No tasks found")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print(" No tasks to delete")
        else:
            task_no = int(input("Enter task number to delete: "))
            removed_task = tasks.pop(task_no - 1)
            print(" Task removed:", removed_task)

    elif choice == "4":
        print(" Exiting To-Do List App. Goodbye!")
        break

    else:
        print(" Invalid choice. Please try again.")
