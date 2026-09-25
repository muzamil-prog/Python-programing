import time

# Colors - red terminal background ke liye
WHITE = "\033[97m"
CYAN = "\033[96m"
BRIGHT_GREEN = "\033[92m"
MAGENTA = "\033[95m"
BRIGHT_BLUE = "\033[94m"

RESET = "\033[0m"
BOLD = "\033[1m"

# Lyrics
lyrics = [
    ("This is for you ❤️🕊️", WHITE),
    ("Mujhko de tu mit jaane ❤️🕊️", CYAN),
    (" Ab Khud se dil mil jaane 🥺💔", BRIGHT_GREEN),
    ("Kyunn hai yeh itna 💔🥺", MAGENTA),
    ("Fasla 🤍🥺", BRIGHT_BLUE)
]

# First line - complete
text, color = lyrics[0]

print()
print(f"{color}{BOLD}    {text}    {RESET}")
print()

time.sleep(0.5)

# Remaining lines - word by word
for text, color in lyrics[1:]:

    words = text.split()

    for word in words:

        print(
            f"{color}{BOLD} {word} {RESET}",
            end="",
            flush=True
        )

        time.sleep(0.35)

    print()
    print()

    time.sleep(0.8)
