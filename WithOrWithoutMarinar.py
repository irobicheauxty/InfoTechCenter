# Welcome Branch
# Libraries Imported Here
import sys
import time

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

print(BOLD + CYAN + "\nWelcome Branch - Developer: Ty Robicheaux" + RESET)
print(YELLOW + "\nWelcome to InfoTechCenter V.1.0" + RESET)

x = 0
ellipsis = 0

while x != 20:
    x += 1

    ellipsisMessage = (
        BOLD + CYAN +
        "InfoTechCenter OS Booting" +
        "." * ellipsis +
        RESET
    )

    ellipsis += 1
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()
    time.sleep(0.5)

    if ellipsis == 4:
        ellipsis = 0

    if x == 20:
        print(
            "\n" + BOLD + GREEN +
            "Operating System Booted Up - Retina Scanned - Access Granted" +
            RESET
        )
