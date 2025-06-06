# daily_reminder.py

# Prompt for task description
task = input("Enter your task: ")

# Prompt for task priority
priority = input("Priority (high/medium/low): ").strip().lower()

# Prompt for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Use match-case to handle different priorities
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Modify the reminder based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Display the reminder
print("\nReminder:", message)
