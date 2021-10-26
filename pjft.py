import pygame, random

from pygame.constants import K_DOWN

#Initialize Pygame
pygame.init()

#ไอคอนเกมและชื่อ
pygame.display.set_caption (' Project Typing Game ') #ชื่อเกม
#icon = pygame.image.load ('game.png') #เปลี่ยนไอคอนเกม
#pygame.display.set_icon (icon)


x = 600
y = 400

speed = 0.05
purple = (170, 0, 200)
darkblue = (0,20,90)
background = (200, 200, 250)
point = 0
pressedword = ""

#ฟังก์ชั่นคำศัพท์
def new_word():
    global chosenword, pressedword, word_x, word_y, text, pointcount, speed
    word_x = random.randint(100, 500)
    word_y = 0
    speed += 0.005
    pressedword = ""
    lines = open("words.txt").read().splitlines()
    chosenword = random.choice(lines)
    text = font.render(chosenword, True, purple)
font = pygame.font.SysFont("CosmicSansMs", 32)
screen = pygame.display.set_mode((x, y))
new_word()
running = True
#Game loop
while running:  
    screen.fill(background)
    word_y += speed
    screen.blit(text, (word_x, word_y))
    text 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pressedword += pygame.key.name(event.key)
            if chosenword.startswith(pressedword):
                if chosenword == pressedword:
                    point += 1
                    new_word()
            else:
                pressedword = ""

    pointcaption = font.render(str(point), True, darkblue)
    screen.blit(pointcaption, (10,5))
    again = font.render(str("KeyDown To Try Again!!"), True, darkblue)
    if word_y < y-5:
        pygame.display.update()
    else:
        event = pygame.event.wait()
        screen.blit(again, (150,250))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN: #ลูกศรลงเพื่อรีสตาร์ทเกม
            speed = 0.05
            point = 0
            new_word()
    pygame.display.update()
