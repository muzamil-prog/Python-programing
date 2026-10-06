import pygame
import time

pygame.init()

# Create window
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("My Song Lyrics")

# Colors
RED = (255, 80, 80)
BLUE = (80, 150, 255)
GREEN = (80, 220, 120)
PURPLE = (190, 100, 255)

# Font
font = pygame.font.Font(None, 50)

# Lyrics
# (time in seconds, sentence, color)
lyrics = [
    (0, "This is for you ❤️ 🕊️", RED),
    (4, "Mujhko de tu mit jaane ❤️ 🕊️", BLUE),
    (8, "Khud se dil mil jaane 🥺 💔", GREEN),
    (12, "Kyunn hai yeh itna 💔 🥺", PURPLE),
    (16, "Fasla 🤍 🥺", RED),
]

clock = pygame.time.Clock()
start_time = time.time()

running = True
last_lyric = None

while running:

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Current time
    current_time = time.time() - start_time

    # Background
    screen.fill((15, 15, 25))

    # Find current lyric
    current_lyric = None

    for lyric in lyrics:
        start, text, color = lyric

        if current_time >= start:
            current_lyric = lyric

    # Show lyric
    if current_lyric:
        start, text, color = current_lyric

        # Print lyric in PowerShell only when it changes
        if current_lyric != last_lyric:
            print(f"[{current_time:.1f}s] {text}")
            last_lyric = current_lyric

        text_surface = font.render(text, True, color)

        # Bottom center
        text_rect = text_surface.get_rect(
            center=(
                screen.get_width() // 2,
                screen.get_height() - 60
            )
        )

        screen.blit(text_surface, text_rect)

    pygame.display.flip()

    # 60 FPS
    clock.tick(60)

pygame.quit()

print("Program finished.")
