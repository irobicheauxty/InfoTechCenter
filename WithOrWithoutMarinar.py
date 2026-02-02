# Gasoline Branch
# Smart Car Fuel & Gas Station Simulation
# ============================================

import random
import time


# -------- Gas Level System --------
def get_gas_level():
    """
    Determines the current gas level in the car.
    Gas level is represented as a percentage (0–100).
    """
    # Random gas level to simulate a fuel sensor
    gas_level = random.randint(5, 100)
    return gas_level


# -------- Gas Station Data --------
def get_gas_stations():
    """
    Creates a list of nearby gas stations.
    Each gas station is represented as a dictionary.
    """

    gas_stations = [
        {
            "name": "Shell",
            "price": 3.49,
            "distance": 5,      # miles
            "open": True,
            "slurpee": False
        },
        {
            "name": "Chevron",
            "price": 3.39,
            "distance": 8,
            "open": True,
            "slurpee": False
        },
        {
            "name": "7-Eleven",
            "price": 3.59,
            "distance": 3,
            "open": True,
            "slurpee": True
        },
        {
            "name": "Speedway",
            "price": 3.29,
            "distance": 10,
            "open": False,
            "slurpee": True
        }
    ]

    return gas_stations


# -------- Alarm System (Fictional) --------
def update_alarm(reason):
    """
    Simulates updating the user's alarm if extra time is needed.
    """
    print("\n[Alarm System]")
    print("⏰ Alarm Updated")
    print(f"Reason: {reason}")
    print("New Alarm Time: 20 minutes earlier than usual")


# -------- Gas Decision System --------
def gasoline_branch():
    """
    Main gasoline logic system.
    Determines if gas is needed and selects the best gas station.
    """

    # Step 1: Determine current gas level
    gas_level = get_gas_level()

    print("\n==============================")
    print("⛽ [Gasoline Branch Online]")
    print("==============================")
    print(f"Current gas level: {gas_level}%")

    # Step 2: Check if gas is below 1/4 tank (25%)
    if gas_level >= 25:
        print("✅ Gas level sufficient. No need to stop for gas.")
        return

    print("⚠️ Gas level below 25%. Gas required.")

    # Step 3: Get list of nearby gas stations
    gas_stations = get_gas_stations()

    # Step 4: Filter only open gas stations
    open_stations = [station for station in gas_stations if station["open"]]

    if not open_stations:
        print("❌ No gas stations are currently open.")
        update_alarm("No open gas stations nearby")
        return

    # Step 5: Determine which stations are reachable
    # Assumption: 1% gas ≈ 1 mile of range (fictional logic)
    max_distance = gas_level

    reachable_stations = [
        station for station in open_stations
        if station["distance"] <= max_distance
    ]

    if not reachable_stations:
        print("❌ Cannot reach any open gas stations with current gas level.")
        update_alarm("Need emergency fuel stop")
        return

    # Step 6: Choose the cheapest reachable gas station
    cheapest_station = min(
        reachable_stations,
        key=lambda station: station["price"]
    )

    # Step 7: Display selected gas station info
    print("\nSelected Gas Station:")
    print(f"Name     : {cheapest_station['name']}")
    print(f"Price    : ${cheapest_station['price']}/gal")
    print(f"Distance : {cheapest_station['distance']} miles")

    # Step 8: Check for snacks and Slurpee
    if cheapest_station["slurpee"]:
        print("🥤 Slurpee available!")
    else:
        print("❌ No Slurpee available.")

    print("🍿 Snacks available")

    # Step 9: Update alarm because a gas stop is required
    update_alarm("Gas stop required before destination")


# -------- Program Start --------
gasoline_branch()
