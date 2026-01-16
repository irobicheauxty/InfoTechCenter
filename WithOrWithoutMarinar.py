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
