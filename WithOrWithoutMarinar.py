#Weather Branch

import random

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


def car_speed_control(speed_limit):
    """
    Simulates a car adjusting its speed based on weather conditions.
    """
    weather = get_random_weather()

    # Define speed adjustments based on weather
    if weather == "Sunny":
        allowed_speed = speed_limit
    elif weather == "Cloudy":
        allowed_speed = int(speed_limit * 0.9)
    elif weather == "Rainy":
        allowed_speed = int(speed_limit * 0.7)
    elif weather == "Foggy":
        allowed_speed = int(speed_limit * 0.6)
    elif weather == "Snowy":
        allowed_speed = int(speed_limit * 0.5)
    elif weather == "Stormy":
        allowed_speed = int(speed_limit * 0.4)

    # Car "talking" output
    print("\n[Car System]")
    print(f"Weather detected: {weather}")
    print(f"Speed limit: {speed_limit} mph")
    print(f"Recommended maximum speed: {allowed_speed} mph")

    return allowed_speed


# -------- Program Start --------
speed_limit = 65  # Pretend road speed limit
car_speed_control(speed_limit)
