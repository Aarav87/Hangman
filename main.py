import pygame
import random
import math
from menu import menu
from game_result import game_end

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman For Noobs')

# load images
images = []
for i in range(7):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

# design
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (163, 73, 164)
BLUE = (63, 72, 204)
LIGHT_BLUE = (0, 162, 232)
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# get random word
def get_word(difficulty):
    if difficulty == "Easy":
        with open('wordlists/easy_wordlist.txt') as f:
            word = list(random.choice(f.readlines()))
        del word[-1]
        word = ''.join(word).upper()

        return word
    if difficulty == "Medium":
        with open('wordlists/medium_wordlist.txt') as f:
            word = list(random.choice(f.readlines()))
        del word[-1]
        word = ''.join(word).upper()

        return word
    if difficulty == "Hard":
        with open('wordlists/hard_wordlist.txt') as f:
            word = list(random.choice(f.readlines()))
        del word[-1]
        word = ''.join(word).upper()

        return word


def draw(word, guessed, hangman_status, letters, RADIUS):
    win.fill(WHITE)

    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def main(difficulty):
    guessed = []
    word = get_word(difficulty)
    print(word)
    hangman_status = 0

    RADIUS = 20
    GAP = 15
    letters = []
    startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
    starty = 400
    A = 65
    for i in range(26):
        x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
        y = starty + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, chr(A + i), True])

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw(word, guessed, hangman_status, letters, RADIUS)

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            image = pygame.image.load("images/winner.png")
            game_end(main, win, image, LETTER_FONT)

        if hangman_status == 6:
            image = pygame.image.load("images/loser.png")
            game_end(main, win, image, LETTER_FONT)


menu(main, win, LETTER_FONT)