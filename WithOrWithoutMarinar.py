#BetaTestDev

# ============================================
# Welcome Branch
# InfoTechCenter OS Boot Simulation
# Developer: Ty Robicheaux
# ============================================

# -------- Libraries Imported Here --------
# sys  -> used for writing to the terminal on the same line
# time -> used to add delays (sleep) for animation timing
import sys
import time

# -------- ANSI Color Codes --------
# These codes add color and formatting to terminal text
CYAN = "\033[96m"      # Cyan text color
GREEN = "\033[92m"     # Green text color
YELLOW = "\033[93m"    # Yellow text color
RESET = "\033[0m"      # Resets text color/style to default
BOLD = "\033[1m"       # Makes text bold

# -------- Welcome Messages --------
# Display developer info and program version with color styling
print(BOLD + CYAN + "\nWelcome Branch - Developer: Ty Robicheaux" + RESET)
print(YELLOW + "\nWelcome to InfoTechCenter V.1.0" + RESET)

# -------- Boot Animation Variables --------
x = 0           # Loop counter (controls how long the boot animation runs)
ellipsis = 0    # Controls how many dots appear after "Booting"

# -------- Boot Animation Loop --------
# Runs until x reaches 20 (simulates OS boot time)
while x != 20:
    x += 1  # Increment the loop counter

    # Create the booting message with animated dots
    ellipsisMessage = (
        BOLD + CYAN +
        "InfoTechCenter OS Booting" +
        "." * ellipsis +
        RESET
    )

    ellipsis += 1  # Increase the number of dots

    # Write the message on the same line in the terminal
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()  # Force the output to update immediately

    # Pause to control animation speed
    time.sleep(0.5)

    # Reset dots after reaching 3 (0–3 loop)
    if ellipsis == 4:
        ellipsis = 0

    # When the boot process finishes, display success message
    if x == 20:
        print(
            "\n" + BOLD + GREEN +
            "Operating System Booted Up - Retina Scanned - Access Granted" +
            RESET
        )



# ============================================
# Weather Branch
# Smart Car Weather & Safety Simulation
# ============================================

# -------- Library Imports --------
# random -> used to randomly select a weather condition
# time   -> reserved for delays or timing (not heavily used yet,
#           but useful for future expansion like animations)
import random
import time


# -------- Weather System --------
def get_random_weather():
    """
    Selects and returns a random weather condition from a predefined list.
    This simulates a weather sensor or weather API in a real system.
    """

    # List containing possible weather states
    weather_conditions = [
        "Sunny",    # Clear weather, safest driving conditions
        "Cloudy",   # Overcast but generally safe
        "Rainy",    # Reduced traction and visibility
        "Stormy",   # Severe weather with high risk
        "Snowy",    # Slippery roads and poor control
        "Foggy"     # Limited visibility
    ]

    # Randomly choose and return one weather condition
    return random.choice(weather_conditions)


# -------- Phone System (Fictional) --------
def send_phone_notification(message):
    """
    Simulates sending a notification to the user's phone.
    This does NOT send a real message; it only prints output
    to represent phone communication in this simulation.
    """

    # Display phone system header
    print("\n[Phone System]")

    # Show notification status
    print("📱 Notification Sent:")

    # Display the notification message
    print(f"Message: {message}")


def update_alarm(new_time):
    """
    Simulates updating the user's phone alarm.
    Used when weather conditions require leaving earlier.
    """

    # Display alarm system header
    print("\n[Alarm System]")

    # Indicate that the alarm has been changed
    print("⏰ Alarm Updated")

    # Show the new alarm time (fictional)
    print(f"New Alarm Time: {new_time}")


# -------- Car System --------
def car_speed_control(speed_limit):
    """
    Simulates a car's decision-making system that:
    - Reads weather conditions
    - Adjusts driving speed for safety
    - Determines risk level
    - Communicates with the user's phone if needed
    """

    # Get current weather from the weather system
    weather = get_random_weather()

    # -------- Speed & Risk Logic --------
    # Adjust allowed speed and risk level based on weather
    if weather == "Sunny":
        allowed_speed = speed_limit      # Full speed allowed
        risk_level = "Low"
    elif weather == "Cloudy":
        allowed_speed = int(speed_limit * 0.9)
        risk_level = "Low"
    elif weather == "Rainy":
        allowed_speed = int(speed_limit * 0.7)
        risk_level = "Medium"
    elif weather == "Foggy":
        allowed_speed = int(speed_limit * 0.6)
        risk_level = "High"
    elif weather == "Snowy":
        allowed_speed = int(speed_limit * 0.5)
        risk_level = "High"
    elif weather == "Stormy":
        allowed_speed = int(speed_limit * 0.4)
        risk_level = "Severe"

    # -------- Car System Display --------
    # Output information as if shown on a car dashboard
    print("\n==============================")
    print("🚗 [Car System Online]")
    print("==============================")
    print(f"Weather detected : {weather}")
    print(f"Road speed limit : {speed_limit} mph")
    print(f"Safe speed       : {allowed_speed} mph")
    print(f"Risk level       : {risk_level}")

    # -------- Safety Response Logic --------
    # If weather is dangerous, notify the user's phone
    if risk_level in ["High", "Severe"]:
        send_phone_notification(
            f"Bad weather detected: {weather}. "
            "Driving conditions are unsafe. Leave earlier to arrive safely."
        )

        # Update the alarm to allow extra travel time
        update_alarm("30 minutes earlier than usual")

    # If weather risk is moderate, send a warning only
    elif risk_level == "Medium":
        send_phone_notification(
            f"Weather conditions: {weather}. "
            "Expect slower travel time. Plan accordingly."
        )

    # If conditions are safe, no action is required
    else:
        print("\n[System Status]")
        print("✅ Conditions normal. No alarm update needed.")

    # Return the allowed speed for potential future use
    return allowed_speed


# -------- Program Start --------
# Define the road speed limit (fictional scenario)
speed_limit = 65  # mph

# Start the car weather and safety simulation
car_speed_control(speed_limit)

