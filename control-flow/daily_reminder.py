# daily_reminder.py

# Prompt for task info
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task based on priority and time sensitivity
if priority == "high":
    priority_msg = "high"
elif priority == "medium":
    priority_msg = "medium"
elif priority == "low":
    priority_msg = "low"
else:
    priority_msg = "normal"

# Customized reminder
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_msg} priority task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {priority_msg} priority task. Consider completing it when you have free time.")


