import pygame
import random

names = [
    "Ananthan", "Aashish", "Abhijith", "Abhiram", "Adhish", "Adithya", "Afnan",
    "Akshith", "Albert", "Alecia", "Alfas", "Amal", "Ameena", "Anjana", "Ann",
    "Anuvind", "Archa", "Ardra", "Arjun", "Ashish", "Athul", "Avani", "Aravind",
    "Darsana", "Dev", "Dhiya", "Diya", "Fathima", "Fuad", "Giridhar",
    "Harigovind", "Harinand", "Jack", "Joel", "Jyothika", "Mathew", "Shameel",
    "Sinan", "Nandana", "Navaneeth", "Nihala", "Nimran", "Nourin", "Prince",
    "Renajith", "Rithurag", "Rukma", "Saaju", "Sabith", "Sandra", "Sayooj",
    "Shahul", "Shawn", "Shon", "Sivaganga", "Sreebala", "Sreekumar",
    "Sreenandan", "Sreraam", "Sritha", "Swalah", "Thejal", "Tom", "Vani",
    "Vinayak", "Vismai", "Viswaik", "Wafa", "Yashvardhan"
]
pygame.init()
win_sound = pygame.mixer.Sound("AudioTranscriberAI_Children Yay Sound Effect (HD).wav")
lose_sound = pygame.mixer.Sound("AudioTranscriberAI_Fahhh - Sound Effect for Meme Edits.wav")
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 40)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)

letters = []
for i in range(26):
    x = 70 + 55 * (i % 13)
    y = 400 + 55 * (i // 13)
    letters.append([x, y, chr(65 + i), True])  

images = []
for i in range(7):
    images.append(pygame.image.load("hangman" + str(i) + ".png"))

hangman_status = 0                      
word = random.choice(names).upper()     
guessed = []                            

def draw():
    win.fill(WHITE)

    title = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(title, (WIDTH / 2 - title.get_width() / 2, 20))

    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (380, 200))

    for x, y, ltr, visible in letters:
        if visible:
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            for letter in letters:
                x, y, ltr, visible = letter
                # Clicked if the mouse is within 25 pixels of the letter
                if visible and abs(x - mouse_x) < 25 and abs(y - mouse_y) < 25:
                    letter[3] = False       # hide the letter
                    guessed.append(ltr)
                    if ltr not in word:
                        hangman_status += 1

    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False

    if won:
        win_sound.play()
        display_message("You WON!")
        display_message("It was " + word)
        pygame.time.delay(1000)
        pygame.quit()

    # Did the player lose?
    if hangman_status == 6:
        lose_sound.play()
        display_message("You LOST! It was " + word)
        pygame.time.delay(1000)
        pygame.quit()

