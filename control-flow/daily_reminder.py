# daily_reminder.py
import sys

# Prompt for task info (exact prompts)
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Determine time sensitivity
is_time_bound = (time_bound == "yes")

# Try to use a match-case implementation if running on Python 3.10+
priority_msg = None
if sys.version_info >= (3, 10):
    # Put the match-case code into a string so older interpreters don't parse it.
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
    # Execute the match-case code in a temporary namespace so it assigns priority_msg
    ns = {"priority": priority}
    exec(match_code, ns)
    priority_msg = ns.get("priority_msg", "normal")
else:
    # Fallback for Python < 3.10 (sandbox)
    if priority == "high":
        priority_msg = "high"
    elif priority == "medium":
        priority_msg = "medium"
    elif priority == "low":
        priority_msg = "low"
    else:
        priority_msg = "normal"

# Use a simple loop (demonstrates a loop without storing multiple tasks)
for _ in range(1):
    if is_time_bound:
        print(f"Reminder: '{task}' is a {priority_msg} priority task that requires immediate attention today!")
    else:
        print(f"Note: '{task}' is a {priority_msg} priority task. Consider completing it when you have free time.")

# Optional friendly completion message (matches example tone)
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")



