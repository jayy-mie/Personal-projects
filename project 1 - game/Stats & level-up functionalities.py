import random
from Gear import HP_Buff, MP_Buff, Speed_Buff, Phys_Def_Buff, Mag_Def_Buff, Phys_Att_Buff, Mag_Att_Buff

#Create the stats and how they relate
class Stats ():
    def __init__(self,Level,HP,MP,BP,Vitality,Strength,Reflexes,Intelligence,Accuracy,Speed,Physical_defense,Magical_defense,Physical_attack,Magical_attack,EXP,Max_EXP):
        self.level = Level
        base_HP = 50
        self.HP = base_HP + (Vitality/2) + HP_Buff + HP
        base_MP = 50
        self.MP = base_MP + (Intelligence/5) + MP_Buff + MP
        self.BP = 0 + BP#The goal is that this should accumulate every turn an offensive move is used.The amount will differ from move to move
        self.Vitality = Vitality
        self.Strength = Strength
        self.Reflexes = Reflexes
        self.Intelligence = Intelligence
        self.Accuracy = Accuracy
        base_speed = 10
        self.Speed = base_speed + (Reflexes/2) + Speed_Buff + Speed
        base_Physical_defense = 10
        self.Physical_defense = base_Physical_defense + (Strength/2) + Phys_Def_Buff + Physical_defense
        base_magical_defense = 10
        self.Magical_defense = base_magical_defense + (Intelligence/2) + Mag_Def_Buff + Magical_defense
        base_Physical_attack = 10
        self.Physical_attack = base_Physical_attack + Strength + Phys_Att_Buff + Physical_attack
        base_magical_attack = 10
        self.Magical_attack = base_magical_attack + Intelligence + Mag_Att_Buff + Magical_attack
        self.EXP = EXP
        self.Max_EXP = Max_EXP

    def Level_Up(self):
        self.level += 1
        self.EXP == 0
        self.Max_EXP = int(self.Max_EXP *1.3)
        self.Stat_Points == 3
        if self.level % 2 == 0:
            self.Skill_Points += 1

    def Gain_EXP(self, EXP_Points):
        self.EXP +=EXP_Points
        if self.EXP >= self.Max_EXP:
            self.Level_Up

class Skill_Points():
    def __init__(self):
        self.Skill_points == 0
    
    def Add_Skill_Points(self, amount):
        self.Skill_Points =+ amount

    def Use_Skill_Points(self, amount):
        if self.Skill_Points >= amount:
            self.Skill_Points -= amount
            return True
        else:
            return False

class Stat_Points():
    def __init__(self):
        self.Stat_Points = {
            'Vitality' : 0,
            'Strength' : 0,
            'Reflexes' : 0,
            'Intelligence' : 0,
            'Accuracy' : 0,
        }

    def Allocate_Stat_Points(self, stat_name, amount):
        if stat_name in self.Stat_Points and amount >= 0:
            self.Stat_Points[stat_name] += amount
            return True
        else:
            return False
        