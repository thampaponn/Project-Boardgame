import pygame, sys
import random
from tkinter import *
from pygame import mixer
import os

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Arcade Python Board Game') #game window name
screen = pygame.display.set_mode((1280, 720), 0, 32)
icon = pygame.image.load('images/icon.png') #icon image
pic1 = pygame.image.load('images/logo3.png') #rps image
pic2 = pygame.image.load('images/logo2.png') #hangman image
pic3 = pygame.image.load('images/logo1.png') #tictactoe image
pic4 = pygame.image.load('images/logo4.png') #fast typing image
pic5 = pygame.image.load('images/logo5.png') #num guessing image
pic8 = pygame.image.load('images/logo8.png') #exit button image
background = pygame.image.load('images/background.png') # background images
pygame.display.set_icon(icon) #window icon
MainMenu = pygame.mixer.Sound('sounds/mainmenu1.mp3')
sss = pygame.mixer.Sound('sounds/click.mp3')
MainMenu.set_volume(0.20)

global click
click = False
 
def main_menu():
    while True:
        global click
        screen = pygame.display.set_mode((1280, 720), 0, 32)
        MainMenu.play()
        screen.blit(background, (0, 0))
        screen.blit(pic1, (110, 197))
        screen.blit(pic2, (462, 197))
        screen.blit(pic3, (814, 197))
        screen.blit(pic4, (285, 399))
        screen.blit(pic5, (637, 399))
        screen.blit(pic8, (1190, 630))
        
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(110, 197, 350, 200)
        button_2 = pygame.Rect(462, 197, 350, 200)
        button_3 = pygame.Rect(814, 197, 350, 200)
        button_4 = pygame.Rect(285, 399, 350, 200)
        button_5 = pygame.Rect(637, 399, 350, 200)
        button_8 = pygame.Rect(1190, 630, 80, 80)

        if button_1.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.load('sounds/click.mp3')
                pygame.mixer.music.play()
                pygame.mixer.pause()
                rockpasci()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.load('sounds/click.mp3')
                pygame.mixer.music.play()
                pygame.mixer.pause()
                hang()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.load('sounds/click.mp3')
                pygame.mixer.music.play()
                pygame.mixer.pause()
                tict()
        if button_4.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.load('sounds/click.mp3')
                pygame.mixer.music.play()
                pygame.mixer.pause()
                fast()
        if button_5.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.load('sounds/click.mp3')
                pygame.mixer.music.play()
                pygame.mixer.pause()
                snake()
        if button_8.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.load('sounds/click.mp3')
                pygame.mixer.music.play()
                pygame.quit()
                sys.exit()
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
   
def rockpasci():
    pygame.mixer.music.load('sounds/menu4.mp3')
    pygame.mixer.music.play(-1, 0)
    pygame.mixer.music.set_volume(0.25)
    os.system('python RockPaSci.py')
    pygame.mixer.music.stop()
    pygame.mixer.unpause()

def snake():
    pygame.mixer.music.load('sounds/menu5.mp3')
    pygame.mixer.music.play(-1, 0)
    pygame.mixer.music.set_volume(0.25)
    os.system('python snake.py')
    pygame.mixer.music.stop()
    pygame.mixer.unpause()
    
def tict():
    pygame.mixer.music.load('sounds/menu1.mp3')
    pygame.mixer.music.play(-1, 0)
    pygame.mixer.music.set_volume(0.25)
    os.system('python tictactoe.py')
    pygame.mixer.music.stop()
    pygame.mixer.unpause()

main_menu()
