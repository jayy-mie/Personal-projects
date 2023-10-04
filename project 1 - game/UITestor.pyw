import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Level-Up Test")

Player_Stats = {
    "Level" : 1,
    "EXP" : 0,
    "Max EXP" : 100,
    "Skill Points" : 0,
}

def Level_Up():
    Player_Stats["EXP"] = 0
    Player_Stats["Level"] += 1
    Player_Stats["Max EXP"] = int(Player_Stats["Max EXP"] * 1.3)
    Player_Stats["Skill Points"] = 1

clock = pygame.time.Clock()
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Level_Up()

    screen.fill(WHITE)

    text = FONT.render(f"Level: {Player_Stats['Level']}", True, (0, 0, 0))
    screen.blit(text, (20, 20))
    text = FONT.render(f"EXP: {Player_Stats['EXP']}", True, (0, 0, 0))
    screen.blit(text, (20, 60))
    text = FONT.render(f"Skill Points: {Player_Stats['Skill Points']}", True, (0, 0, 0))
    screen.blit(text, (20, 100))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()
