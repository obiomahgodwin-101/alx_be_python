# daily_reminder.py

# Ask the user for task details
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
priority = input("Enter priority (high/medium/low): ").strip().lower()

# Determine if immediate action is needed
immediate = ""
if time_bound == "yes":
    immediate = " — Immediate action required!"

# Handle priority levels using if-elif-else
if priority == "high":
    priority_msg = "High Priority"
elif priority == "medium":
    priority_msg = "Medium Priority"
elif priority == "low":
    priority_msg = "Low Priority"
else:
    priority_msg = "Normal Priority"

# Print the customized reminder
print(f"Reminder: {task} [{priority_msg}]{immediate}")




