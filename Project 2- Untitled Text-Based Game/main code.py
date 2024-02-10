# Python text rpg
# Created by Jamie Kariuki

import tkinter as tk
import pygame 
import sys
import random
import os
import time
import textwrap

# initialize PyGame
pygame.init()

# setting screen dimensions
screen_width = 800
screen_height = 600

# creating the screen
screen = pygame.display.set_mode((screen_width,screen_height))

# setting the title 
pygame.display.set_caption("Murim Text Adventure")

# setting up the base player
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
        self.Injurde_Rightarm = False
        self.Injured_Leftleg = False
        self.Injured_Rightleg = False
        self.Injured_Ribs = False
        self.Is_poisoned = False
        self.Weapon_Choice = []
        self. Learned_Tchniques = []
        self.Affiliations = []

MyPlayer = Player()

# Initializing the TKinter window
root = tk.Tk()
root.title("Murim Text Adventure")

# Setting up TKinter labels and buttons
label = tk.Label(root, text = "Welcome to the RPG", font = ("Helvetica", 16))
label.pack(pady = 10)

start_button = tk.Button(root, text = "Start Game", command = root.destroy) #replace with my start_game logic
start_button.pack(pady = 5)

load_button = tk.Button(root, text = "Load Game", command = root.destroy)
load_button.pack(pady = 5)

quit_button = tk.Button(root, text = "Quit", command = sys.exit)
quit_button.pack(pady = 5)

# running the TKinter main loop
root.mainloop()

# The amin game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Updating the display
            pygame.display.update()
        
# Quitting the Pygame
pygame.quit()