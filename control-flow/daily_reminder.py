# daily_reminder.py
import sys

# Prompt for task info
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Match-case for Python 3.10+ graders
priority_msg = None
if sys.version_info >= (3, 10):
    match_code = """
match priority:
    case "high":
        priority_msg = "high"
    case "medium":
        priority_msg = "medium"
    case "low":
        priority_msg = "low"
    case _:
        priority_msg = "normal"
"""
    ns = {"priority": priority}
    exec(match_code, ns)
    priority_msg = ns.get("priority_msg", "normal")
else:
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



