import pygame, random

from pygame.constants import K_DOWN
from wordsforhangman import word_list

#Initialize Pygame
pygame.init()
pygame.mixer.init()

#ไอคอนเกมและชื่อ
pygame.display.set_caption (' Project Typing Game ') #ชื่อเกม
#icon = pygame.image.load ('game.png') #เปลี่ยนไอคอนเกม
#pygame.display.set_icon (icon)
bgpic = pygame.image.load('images/Fast_Typing.png')
ScoreCount = pygame.mixer.Sound('sounds/press.wav')
ScoreCount.set_volume(0.25)

x = 1000
y = 640

speed = 0.15
dark = (0,0,0)
lime = (50,205,50)
purple = (170, 0, 200)
darkblue = (0,20,90)
background = (dark)
color_word = (lime)
point = 0
pressedword = ""

#ฟังก์ชั่นคำศัพท์
def new_word():
    global chosenword, pressedword, word_x, word_y, text, pointcount, speed
    word_x = random.randint(100, 850)
    word_y = 0
    speed += 0.002
    pressedword = ""
    words = [random.choice(word_list).lower()]
    chosenword = random.choice(words)
    text = font.render(chosenword, True, color_word)
font = pygame.font.SysFont("Consolas", 35)
gameoverfont = pygame.font.SysFont("Consolas", 180)
scoreboardfont = pygame.font.SysFont("Consolas", 90)
screen = pygame.display.set_mode((x, y))
new_word()
# word
def display_message(message1,message2,message3):
    screen.fill(background)
    text1 = gameoverfont.render(message1, 1, lime)
    text2 = scoreboardfont.render(message2, 1, lime)
    text3 = scoreboardfont.render(message3, 1, lime)
    screen.blit(text1, (x/2 - text1.get_width()/2, y/8 - text1.get_height()/10))
    screen.blit(text2, (x/2 - text2.get_width()/2, y/2 - text2.get_height()/2))
    screen.blit(text3, (x/2 - text3.get_width()/2, y/1.5 - text3.get_height()/10))
    pygame.display.update()
    pygame.time.delay(500)
running = True

#Game loop
while running:  
    screen.blit(bgpic, (0, 0))
    word_y += speed
    screen.blit(text, (word_x, word_y))
    word_pressed = '>>>'
    word_pressed += pressedword
    text1 = font.render(word_pressed, 1, (50, 250, 50))
    screen.blit(text1, (x/2 - text1.get_width()/2, 550))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pressedword += pygame.key.name(event.key)
            if chosenword.startswith(pressedword):
                if chosenword == pressedword:
                    point += 1
                    ScoreCount.play()#เสียงตอนพิมพ์ถูก
                    new_word()
            else:
                pressedword = ""
    finalscore = 'Your SCORE:'
    pointcaption = font.render(str(point), True, color_word)##ตัวนับคะแนน
    screen.blit(pointcaption, (10,5))
    if word_y < y-5:
        pygame.display.update()
    else:
        event = pygame.event.wait()
        finalscore += str(point)
        display_message("GAME OVER", finalscore, "Press R & Try Again!")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r: #ลูกศรลงเพื่อรีสตาร์ทเกม
            speed = speed
            point = 0
            new_word()
    pygame.display.update()
