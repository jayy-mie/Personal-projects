#Python Text RPG
#By: Jamie Kariuki

import cmd
import textwrap
import sys
import os
import time
import random
import tkinter as tk

screen_width = 100

# Player Setup #

class Player:
    def __init__(self) -> None:
        self.Gender = ''
        self.FirstName = ''
        self.SecondName = ''
        self.hp = 50
        self.stamina = 50
        self.InnerQi = 100
        self.MartialLevel = ''
        self.Strength = 10
        self.Endurance = 10
        self.Stamina = 10
        self.Perception = 10
        self.Charisma = 10
        self.Injured_leftarm = leftarm
        self.Injured_rightarm = rightarm
        self.Injured_leftleg = leftleg
        self.Injured_rightleg = rightleg
        self.Injured_ribs = ribs
        self.Is_poisoned = poisoned
        self.Learned_Techniques = []

MyPlayer = Player()


#Title Screen#


