# Python text rpg
#Created by Jamie Kariuki

import pygame
import sys
import random

# Initializing pygame
pygame.init()

# Setting game dimensions
screen_width = 800
screen_height = 600

# Setting the title
pygame.display.set_caption("Murim Text Adventure")

# Creating the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Setting up the base player character
class Player:
    def __init__(self):
       self.Gender = ''
       self.FirstName = ''
       self.SecondName = ''
       self.hp = 50
       self.stamina = 50
       self.Qi = 100
       self.MartialLevel = ''
       self.Strength = 10 
       self.Endurance = 10
       self.Stamina = 10
       self.Perception = 10
       self.Charisma = 10
       self.Intelligence = 10
       self.Injured_Leftarm = False
       self.Injured_Rightarm = False
       self.Injured_Leftleg = False
       self.Injured_Rightleg = False
       self.Injured_Ribs = False
       self.Is_poisoned = False
       self.Weapon_Choice = []
       self.Learned_Tachniques = []
       self.Affiliations = []

MyPlayer = Player()

# Setting up the font
font = pygame.font.Font(None, 36)

# Setting up the text rendering function
def textrender(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Creating a class for buttons
class Button:
    def __init__(self, text, x, y, width, height, command):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.command = command

    def draw(self):
        pygame.draw.rect(screen, (255, 0 ,0), (self.x, self.y, self.width, self.height))
        textrender(self.text, (255, 255, 255), self.x + 10, self.y + 10)

# Creating the start button
start_button = Button("Start Game", 200, 200, 200, 50, lambda: print("Game started!"))

# Creating the load button
load_button = Button("Load Game", 200, 300, 200, 50, lambda: print("Game loaded!"))

# creating the quit button
quit_button = Button("Quit", 200, 400, 200, 50, sys.exit)

# Creating the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if start_button.x < mouse_x < start_button.x + start_button.width and start_button.y < mouse_y < start_button.y + start_button.height :
                start_button.command()
            elif load_button.x < mouse_x < load_button.x + load_button.width and load_button.y < mouse_y < load_button.y + load_button.height:
                load_button.command()
            elif quit_button.x < mouse_x < quit_button.x + quit_button.width and quit_button.y < mouse_y < quit_button.y + quit_button.height:
                quit_button.command()

# Crearing the screen
    screen.fill((255, 255, 255))

# Drawing buttons
    start_button.draw()
    load_button.draw()
    quit_button.draw()

# Updating the display
    pygame.display.update()

# Quit pygame
pygame.quit()