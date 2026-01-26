#Weather Branch

import random

def get_random_weather():
    """
    Returns a random weather condition from a predefined list.
    """
    weather_conditions = [
        "Sunny",
        "Cloudy",
        "Rainy",
        "Stormy",
        "Snowy",
        "Windy",
        "Foggy"
    ]

    return random.choice(weather_conditions)


# Call the function and print the result
current_weather = get_random_weather()
print("Today's weather condition is:", current_weather)
