import pygame
from settings import settings

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (163, 73, 164)
BLUE = (63, 72, 204)
LIGHT_BLUE = (0, 162, 232)

def game_end(main, win, image, LETTER_FONT):
    while True:
        play_again_button = pygame.Rect(130, 250, 160, 50)
        play_again_button_text = LETTER_FONT.render('Play Again', 1, BLACK)
        settings_button = pygame.Rect(305, 250, 160, 50)
        settings_button_text = LETTER_FONT.render('Settings', 1, BLACK)
        exit_button = pygame.Rect(480, 250, 160, 50)
        exit_button_text = LETTER_FONT.render('Exit', 1, BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if settings_button.collidepoint(event.pos):
                        difficulty = settings(win, LETTER_FONT)
                    if play_again_button.collidepoint(event.pos):
                        main(difficulty)
                    if exit_button.collidepoint(event.pos):
                        pygame.quit()
                        quit()

        win.fill(WHITE)
        win.blit(image, (100, 150))
        pygame.draw.rect(win, PURPLE, play_again_button)
        win.blit(play_again_button_text, (140, 260))
        pygame.draw.rect(win, BLUE, settings_button)
        win.blit(settings_button_text, (330, 260))
        pygame.draw.rect(win, LIGHT_BLUE, exit_button)
        win.blit(exit_button_text, (530, 260))
        pygame.display.update()