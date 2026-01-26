#Weather Branch

import random
import time

# -------- Weather System --------
def get_random_weather():
    """
    Returns a random weather condition.
    """
    weather_conditions = [
        "Sunny",
        "Cloudy",
        "Rainy",
        "Stormy",
        "Snowy",
        "Foggy"
    ]
    return random.choice(weather_conditions)


# -------- Phone System (Fictional) --------
def send_phone_notification(message):
    """
    Simulates sending a message to the user's phone.
    """
    print("\n[Phone System]")
    print("📱 Notification Sent:")
    print(f"Message: {message}")


def update_alarm(new_time):
    """
    Simulates updating the user's phone alarm.
    """
    print("\n[Alarm System]")
    print("⏰ Alarm Updated")
    print(f"New Alarm Time: {new_time}")


# -------- Car System --------
def car_speed_control(speed_limit):
    """
    Simulates car decision-making based on weather conditions.
    """
    weather = get_random_weather()

    # Speed logic based on weather
    if weather == "Sunny":
        allowed_speed = speed_limit
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

    # Display car system output
    print("\n==============================")
    print("🚗 [Car AI System Online]")
    print("==============================")
    print(f"Weather detected : {weather}")
    print(f"Road speed limit : {speed_limit} mph")
    print(f"Safe speed       : {allowed_speed} mph")
    print(f"Risk level       : {risk_level}")

    # If conditions are dangerous, notify phone + update alarm
    if risk_level in ["High", "Severe"]:
        send_phone_notification(
            f"Bad weather detected: {weather}. "
            "Driving conditions are unsafe. Leave earlier to arrive safely."
        )

        # Fake alarm logic
        update_alarm("30 minutes earlier than usual")

    elif risk_level == "Medium":
        send_phone_notification(
            f"Weather conditions: {weather}. "
            "Expect slower travel time. Plan accordingly."
        )

    else:
        print("\n[System Status]")
        print("✅ Conditions normal. No alarm update needed.")

    return allowed_speed


# -------- Program Start --------
speed_limit = 65  # Pretend road speed limit
car_speed_control(speed_limit)
