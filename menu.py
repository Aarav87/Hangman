import pygame
from settings import settings

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (163, 73, 164)
BLUE = (63, 72, 204)
LIGHT_BLUE = (0, 162, 232)

def menu(main, win, LETTER_FONT):
    while True:
        play_button = pygame.Rect(170, 300, 150, 50)
        play_button_text = LETTER_FONT.render('Play', 1, BLACK)
        settings_button = pygame.Rect(335, 300, 150, 50)
        settings_button_text = LETTER_FONT.render('Settings', 1, BLACK)
        quit_button = pygame.Rect(500, 300, 150, 50)
        quit_button_text = LETTER_FONT.render('Quit', 1, BLACK)
        image = pygame.image.load("images/logo.png")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if settings_button.collidepoint(event.pos):
                        difficulty = settings(win, LETTER_FONT)
                    if play_button.collidepoint(event.pos):
                        main(difficulty)
                    if quit_button.collidepoint(event.pos):
                        pygame.quit()
                        quit()

        win.fill(WHITE)
        win.blit(image, (150, 100))
        pygame.draw.rect(win, PURPLE, play_button)
        win.blit(play_button_text, (210, 310))
        pygame.draw.rect(win, BLUE, settings_button)
        win.blit(settings_button_text, (355, 310))
        pygame.draw.rect(win, LIGHT_BLUE, quit_button)
        win.blit(quit_button_text, (540, 310))
        pygame.display.update()