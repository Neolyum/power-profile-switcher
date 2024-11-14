import subprocess
from pystray import Icon, Menu, MenuItem
from PIL import Image
import re

def clean_plan_name(plan_name):
    # Remove trailing " (Active)" or " (Active)*" and any trailing asterisk or brackets
    plan_name = re.sub(r'[)*\s]+$', '', plan_name, flags=re.MULTILINE)
    return plan_name.strip()


# Function to list all available power plans
def list_power_plans():
    plans = {}
    output = subprocess.check_output("powercfg -list", shell=True).decode()
    for line in output.splitlines():
        if "Power Scheme GUID" in line:
            parts = line.split(": ")
            plan_name = clean_plan_name(parts[1].split("  (")[1].strip())
            guid = parts[1].split("  (")[0].strip()
            plans[plan_name] = guid
    return plans

# Function to change the power plan
def set_power_plan(guid):
    subprocess.run(f"powercfg -setactive {guid}", shell=True)

# Initialize power plans dictionary
power_plans = list_power_plans()
current_plan = None

# Detect the current power plan
def get_current_plan():
    global current_plan
    output = subprocess.check_output("powercfg -getactivescheme", shell=True).decode()
    current_plan = [name for name, guid in power_plans.items() if guid in output][0]
    print(f"Current plan is {current_plan}")

get_current_plan()

# Callback function for menu item
def change_plan(icon, item):
    global current_plan
    set_power_plan(power_plans[item.text])
    current_plan = item.text
    print(f"Changing plan to {current_plan}")
    icon.update_menu()

# Build the dynamic menu
def build_menu():
    return Menu(
        *(MenuItem(name, change_plan, radio=True, checked=lambda item: item.text == current_plan)
          for name in power_plans.keys()),
        MenuItem("Quit", lambda icon, item: icon.stop())
    )

# Create the system tray icon
icon = Icon("PowerPlanSwitcher", icon=Image.open("icon.png"), title="Power Plan Switcher", menu=build_menu())

# Run the application
icon.run()