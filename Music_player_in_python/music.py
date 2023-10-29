#Music Player using Python
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Initialize Pygame
pygame.init()

# Set the display dimensions
display_width = 800
display_height = 600

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Music Player')

clock = pygame.time.Clock()

# Load music file
pygame.mixer.music.load('D:\Internship\Code_Clause\Music_player_in_python\leva-eternity-149473.mp3')

# Play the music
pygame.mixer.music.play()

# Loop to keep the music playing
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameDisplay.fill(white)

    # Add any other elements or functionalities here if needed

    pygame.display.update()
    clock.tick(60)
