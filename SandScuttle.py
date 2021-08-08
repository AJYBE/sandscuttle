import pgzrun
import random

WIDTH = 800
HEIGHT = 800

char = Actor('blug')
char.x = 100
char.y = 400

trash1 = Actor('trash_1')
trash1.x = random.randint (1200,1800)
trash1.y = random.randint(20, 780)

trash2 = Actor('trash_1')
trash2.x = random.randint (1400,2000)
trash2.y = random.randint(20, 780)

trashbag = Actor('trashbag')
trashbag.x = random.randint (1600,2200)
trashbag.y = random.randint(20, 780)

pbottle = Actor('pbottle')
pbottle.x = random.randint (1800,2400)
pbottle.y = random.randint (20,780,)

crab = Actor('crab')
crab.x = random.randint (2000,2800)
crab.y = random.randint(20, 780)

background_images = ['beach']
backgrounds = []
background = Actor('beach')
background.x = 2800
background.y = 400
backgrounds.append(background)

score = 0

def update():
    global score
    
    if keyboard.left:
            char.x = char.x - 10
    if keyboard.right:
            char.x = char.x + 10
    if keyboard.up:
            char.y = char.y - 10
    if keyboard.down:
            char.y = char.y + 10

    for background in backgrounds:
        background.x -= 3
        if background.x < -600:
            background.x = 0
            background.image = ('beach')
        trash1.x -= 3
        trash2.x -=3
        pbottle.x -= 3
        trashbag.x -= 3
        crab.x -= 7

    if trash1.colliderect(char):
        trash1.x = random.randint (1400,2200)
        trash1.y = random.randint(20, 780)
        score = score + 1

    if trash2.colliderect(char):
        trash2.x = random.randint (1200,1800)
        trash2.y = random.randint(20, 780)
        score = score + 1

    if trashbag.colliderect(char):
        trashbag.x = random.randint (1300,2500)
        trashbag.y = random.randint(20, 780)
        score = score + 1

    if pbottle.colliderect(char):
        pbottle.x = random.randint (1600,2400)
        pbottle.y = random.randint(20, 780)
        score = score + 1
    
def draw():
    screen.clear()
    for background in backgrounds:
        background.draw()
    char.draw()
    trash1.draw()
    trash2.draw()
    pbottle.draw()
    trashbag.draw()
    crab.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=40)

pgzrun.go()
