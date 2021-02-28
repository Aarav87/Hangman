import pygame
import PygameUtils as pu

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (163, 73, 164)
BLUE = (63, 72, 204)
LIGHT_BLUE = (0, 162, 232)

def settings(win, LETTER_FONT):
    settings = True
    while settings:
        easy_button = pygame.Rect(170, 300, 150, 50)
        easy_button_text = LETTER_FONT.render('Easy', 1, BLACK)
        medium_button = pygame.Rect(335, 300, 150, 50)
        medium_button_text = LETTER_FONT.render('Medium', 1, BLACK)
        hard_button = pygame.Rect(500, 300, 150, 50)
        hard_button_text = LETTER_FONT.render('Hard', 1, BLACK)
        image = pygame.image.load("images/settings.png")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if easy_button.collidepoint(event.pos):
                        return 'Easy'
                    if medium_button.collidepoint(event.pos):
                        return 'Medium'
                    if hard_button.collidepoint(event.pos):
                        return 'Hard'

        win.fill(WHITE)
        win.blit(image, (150, 100))
        pygame.draw.rect(win, PURPLE, easy_button)
        win.blit(easy_button_text, (210, 310))
        pygame.draw.rect(win, BLUE, medium_button)
        win.blit(medium_button_text, (355, 310))
        pygame.draw.rect(win, LIGHT_BLUE, hard_button)
        win.blit(hard_button_text, (540, 310))
        pygame.display.update()
