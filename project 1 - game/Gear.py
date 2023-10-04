class gear_buffs:
    def __init__(self, HP_Buff, MP_Buff, Phys_Att_Buff, Mag_Att_Buff, Phys_Def_Buff, Mag_Def_Buff, Speed_Buff, Accu_Buff, Luck_Buff, Def_from_fire, Def_from_ice, ):
        self.HP_Buff = HP_Buff
        self.MP_Buff = MP_Buff
        self.Phys_Att_Buff = Phys_Att_Buff
        self.Mag_Att_Buff = Mag_Att_Buff
        self.Phys_Def_Buff = Phys_Def_Buff
        self.Mag_Def_Buff = Mag_Def_Buff
        self.Speed_Buff = Speed_Buff
        self.Accu_Buff = Accu_Buff
        self.Luck_Buff = Luck_Buff
        self.Def_from_ice = Def_from_ice
        self.Def_from_fire = Def_from_fire

class Jackets(gear_buffs):
    def __init__(self, HP_Buff, MP_Buff, Phys_Att_Buff, Mag_Att_Buff, Phys_Def_Buff, Mag_Def_Buff, Speed_Buff, Accu_Buff, Luck_Buff, Def_from_fire, Def_from_ice):
        super().__init__(HP_Buff, MP_Buff, Phys_Att_Buff, Mag_Att_Buff, Phys_Def_Buff, Mag_Def_Buff, Speed_Buff, Accu_Buff, Luck_Buff, Def_from_fire, Def_from_ice)

        self.commoners_jackets = {
            'Name' : "Commoner's Jacket",
            'Description' : "A set of clothing used by commoners. Provides the barest defense against the elements.",
            'Phys_Def_Buff' : 5
        },
        self.adventurers_jacket = {
            'Name' : "Adventurer's Jacket",
            'Description' : "A jacket customarily given to the newly-accepted of the Adventurers'Guild.",
            'Phys_Def_Buff' : 7,
            'Luck_Buff' : 3
        },
        self.leather_jacket = {
            'Name' : "Leather Jacket",
            'Description' : "An ordinary jacket, commonly found in almost any town. However, it does offer some semblance of shielding from the cold.",
            'Phys_Def_Buff' : 10,
            'Def_from_ice' : 5
        },
        self.jr_inquisitor_jacket = {
            'Name' : "Junior Inquisitor Jacket",
            'Description' : "A jacket given to junior members of the Inquisitors of Astrala, The Goddess of the stars.",
            'Mag_Def_Buff' : 10,
            'Phys_Def_Buff' : 5
        },
        self.gamblers_jacket = {
            'Name' : "Gambler's Jacket",
            'Description' : "Gamblers walking around the vicity of Astral Amusements are regularly seen wearing this item of clothing. Apparently, they are enchanted with a blessing of good fortune.",
            'Phys_Def_Buff' : 5,
            'Luck_Buff' : 5,
            'Accu_Buff' : 5
        }

class Light_Armor(gear_buffs):
    def __init__(self, HP_Buff, MP_Buff, Phys_Att_Buff, Mag_Att_Buff, Phys_Def_Buff, Mag_Def_Buff, Speed_Buff, Accu_Buff, Luck_Buff, Def_from_fire, Def_from_ice):
        super().__init__(HP_Buff, MP_Buff, Phys_Att_Buff, Mag_Att_Buff, Phys_Def_Buff, Mag_Def_Buff, Speed_Buff, Accu_Buff, Luck_Buff, Def_from_fire, Def_from_ice)

        self.trainee_fatigues = {
            'Name' : "Trainee Fatigues",
            'Descriptions' : "Fatigues worn by knights-in-training of the Eldoria Kingdom.",
            'Phys_Def_Buff' : 6,
        },  
        self.patrolman_armor = {
            'Name' : "Patrolman Armor",
            'Description' : "Armor worn by the night watch of the streets of the Eldoria Kingdom.",
            'Phys_Def_Buff' : 8,
            'Speed_Buff' : 2,
        },
        self.swordsman_armor = {
            'Name' : "Swordsman Armor",
            'Description' : "Chestguard and fatigues worn by wandering swordsmen.",
            'Phys_Def_Buff' : 8,
            'Speed_Buff' : 3,
            'Def_from_fire' : 4,
        },
        self.junior_knight_armor = {
            'Name' : "Knight Armor",
            'Description' : "Armor worn by junior knights of the Eldoria Kingdom.",
            'Phys_Def_Buff' : 10,
            'Acc_Buff' : 3,
            'Mag_Def_Buff' : 2,
        },
        self.mercenary_armor = {
            'Name' : "Mercenary Armor",
            'Description' : "Armor worn by novice mercenaries.",
            'Phys_Def_Buff' : 5,
            'Luck_Buff' : 5,
            'Speed_Buff' : 5,
            'Mag_Def_Buff' : 5,
        }

class robes(gear_buffs):
    def __init__(self, HP_Buff, MP_Buff, Phys_Att_Buff, Mag_Att_Buff, Phys_Def_Buff, Mag_Def_Buff, Speed_Buff, Accu_Buff, Luck_Buff, Def_from_fire, Def_from_ice):
        super().__init__(HP_Buff, MP_Buff, Phys_Att_Buff, Mag_Att_Buff, Phys_Def_Buff, Mag_Def_Buff, Speed_Buff, Accu_Buff, Luck_Buff, Def_from_fire, Def_from_ice)

        self.trainee_robes = {
            
        }        


