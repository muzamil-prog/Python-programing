import pygame
import time

pygame.init()

# ---------------- WINDOW ----------------
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("My Song Lyrics")

# ---------------- COLORS ----------------
WHITE = (255, 255, 255)
RED = (255, 80, 80)
BLUE = (80, 150, 255)
GREEN = (80, 220, 120)
PURPLE = (190, 100, 255)

# ---------------- FONTS ----------------
# Windows emoji font
emoji_font_path = r"C:\Windows\Fonts\seguiemj.ttf"

try:
    font = pygame.font.Font(emoji_font_path, 55)
except:
    font = pygame.font.Font(None, 55)

# ---------------- LYRICS ----------------
# (start time, sentence, color)

lyrics = [
    (0, "This is for you ❤️ 🕊️", RED),
    (5, "Mujhko de tu mit jaane ❤️ 🕊️", BLUE),
    (10, "Khud se dil mil jaane 🥺 💔", GREEN),
    (15, "Kyunn hai yeh itna 💔 🥺", PURPLE),
    (20, "Fasla 🤍 🥺", RED),
]

clock = pygame.time.Clock()

start_time = time.time()

last_sentence = ""
last_word_count = 0

running = True

while running:

    # ---------------- EVENTS ----------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------------- TIME ----------------
    current_time = time.time() - start_time

    # ---------------- BACKGROUND ----------------
    screen.fill((15, 15, 25))

    # ---------------- FIND LYRIC ----------------
    current_lyric = None

    for lyric in lyrics:
        start, sentence, color = lyric

        if current_time >= start:
            current_lyric = lyric

    if current_lyric:

        start, sentence, color = current_lyric

        # Words
        words = sentence.split()

        # Time passed since this sentence started
        sentence_time = current_time - start

        # One new word every 0.6 seconds
        word_count = int(sentence_time / 0.6) + 1

        if word_count > len(words):
            word_count = len(words)

        # Words that should currently be visible
        visible_words = words[:word_count]

        # Join words
        visible_text = " ".join(visible_words)

        # ---------------- POWERSHELL OUTPUT ----------------
        if visible_text != last_sentence:

            print(visible_text)

            last_sentence = visible_text

        # ---------------- TEXT ----------------
        text_surface = font.render(
            visible_text,
            True,
            color
        )

        # CENTER OF SCREEN
        text_rect = text_surface.get_rect(
            center=(
                screen.get_width() // 2,
                screen.get_height() // 2
            )
        )

        screen.blit(text_surface, text_rect)

    # ---------------- UPDATE ----------------
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

print("Program finished.")
