import pygame
import math
import random




# Inicia el pygame
pygame.init()

#el joc s'executa en la resolució nativa i descobrim els valors de l'alçada i amplada
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
x = pygame.display.Info().current_w
y = pygame.display.Info().current_h

#Fons del joc
background = pygame.image.load('ttt.jpg')

#Títol del joc i Logo
pygame.display.set_caption("Air Battle 44")
icon = pygame.image.load('av.png')
pygame.display.set_icon(icon)



# Creem el Jugador
playerImg = pygame.image.load('av.png')
playerX = x/2
playerY = y-320
playerX_change = 0
playerY_change = 0

# Creem la Bala
bulletImg = pygame.image.load('bala.png')
bulletX = 0
bulletY = y-320
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Ready = la podem veure la bala a la pantalla
# Fire = La bala s'està movent


# Creem el marcador
score_value = 0
fontUI = pygame.font.Font('freesansbold.ttf', 32)
fontW = pygame.font.Font(None, 128)
textX = 10
testY = 10


# Creem el Enemic
enemyImg = pygame.image.load('us.png')
enemyX = random.randint(0, x)
enemyY = random.randint(50, 150)
enemyX_change = 1.8
enemyY_change = 0

# Creem el Enemic 2
enemy2Img = pygame.image.load('us.png')
enemy2X = random.randint(0, x)
enemy2Y = random.randint(50, 150)
enemy2X_change = random.randint(1, 3)
enemy2Y_change = 0

# Creem el Enemic 3
enemy3Img = pygame.image.load('us.png')
enemy3X = random.randint(0, x)
enemy3Y = random.randint(50, 150)
enemy3X_change = random.randint(1, 3)
enemy3Y_change = 0

# Creem el Enemic 4
enemy4Img = pygame.image.load('us.png')
enemy4X = random.randint(0, x)
enemy4Y = random.randint(50, 150)
enemy4X_change = random.randint(1, 3)
enemy4Y_change = 0

# Creem el Enemic 5
enemy5Img = pygame.image.load('us.png')
enemy5X = random.randint(0, x)
enemy5Y = random.randint(50, 150)
enemy5X_change = random.randint(1, 3)
enemy5Y_change = 0

start_ticks = 25000

#Aquestes funcions fan que el player, bala, enemic, marcador apareixin
def player(x, y):
    screen.blit(playerImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    #fa que la bala surti centrada en el jugador
    screen.blit(bulletImg, (x + 135, y + 10))

def show_score(x, y):
    score = fontUI.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def timer(x, y):
    #es resta el temps que dura el joc (25000 tics) menys els tics que porta el joc iniciat
    seconds = (start_ticks - pygame.time.get_ticks()) /1000
    timer = fontUI.render(str(seconds), True, (225, 255, 255))
    screen.blit(timer, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def enemy2(x, y):
    screen.blit(enemyImg, (x, y))

def enemy3(x, y):
    screen.blit(enemyImg, (x, y))

def enemy4(x, y):
    screen.blit(enemyImg, (x, y))

def enemy5(x, y):
    screen.blit(enemyImg, (x, y))

#sistema per detectar una colisió
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 135:
        return True
    else:
        return False

# Fem que la finestra del joc funcioni per sempre
running = True
while running:




    #Fons del joc
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Si les fletxes són pressionades canviaran el moviment ( +5) (<-- -5, --> +5)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:

                if bullet_state == "ready":
                    # fa que la bala surti al mateix lloc que el jugador
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        #Si la fletxa ja no és pressionada el moviment és cancel·la
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #limits de la pantalla (si el personatje és a la posició 0 o 1080 eviatara que continui)
    if playerX <= -35:
        playerX = -35
    elif playerX >= x-285:
        playerX = x-285


    #si el personatje mor sera mogut a una posició a la cual no l'hi afectara els limits
    if enemyX <= 0:
        enemyX_change = 1.5
    elif enemyX >= x-212:
        enemyX_change = -1.5
    elif playerX == 55555:
        enemyChangeX = 0

    if enemy2X <= 0:
        enemy2X_change = 1
    elif enemy2X >= x-212:
        enemy2X_change = -1
    elif playerX == 55555:
        enemy2ChangeX = 0

    if enemy3X <= 0:
        enemy3X_change = 2
    elif enemy3X >= x-212:
        enemy3X_change = -2
    elif playerX == 55555:
        enemy3ChangeX = 0

    if enemy4X <= 0:
        enemy4X_change = 2.5
    elif enemy4X >= x-212:
        enemy4X_change = -2.5
    elif playerX == 55555:
        enemy4ChangeX = 0

    if enemy5X <= 0:
        enemy5X_change = 3
    elif enemy5X >= x-212:
        enemy5X_change = -3
    elif playerX == 55555:
        enemy5ChangeX = 0

    # si hi ha hagut una colisió es torna a preparar la bala i es mou al enemic
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        enemyX = 55555
        enemyY = 55555
        enemyChangeX = 0
        score_value += 1503

    collision = isCollision(enemy2X, enemy2Y, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        enemy2X = 55555
        enemy2Y = 55555
        enemy2ChangeX = 0
        score_value += 44

    collision = isCollision(enemy3X, enemy3Y, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        enemy3X = 55555
        enemy3Y = 55555
        enemy3ChangeX = 0
        score_value += 2021

    collision = isCollision(enemy4X, enemy4Y, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        enemy4X = 55555
        enemy4Y = 55555
        enemyChangeX = 0
        score_value += 2019

    collision = isCollision(enemy5X, enemy5Y, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        enemy5X = 55555
        enemy5Y = 55555
        enemy5ChangeX = 0
        score_value += 1024


    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    #es resta el temps que dura el joc (25000 tics) menys els tics que porta el joc iniciat

    seconds = (start_ticks - pygame.time.get_ticks()) /1000

    #Si els segons són inferiors a 0 canviem el fons i posem text
    if seconds <= 0:
        playerX = 55555
        enemyY = 55555
        enemy2Y = 55555
        enemy3Y = 55555
        enemy4Y = 55555
        enemy5X = 55555
        testY = 55555
        screen.fill((0, 0, 0))
        game_over = fontW.render('Game Over', True, (255, 255, 255))
        screen.blit(game_over, (x/2 -240, y/2 -64))

    if score_value == 6611:
        playerX = 5555
        screen.fill((255, 255, 255))
        testY = 55555
        win = fontW.render('You Win', True, (0, 0, 0))
        screen.blit(win, (x/2 -160, y/2 -32))

    #tots els textos
    show_score(textX, testY)
    timer(testY, testY+40)

    #moviment del jugador i dels enemics

    playerX += playerX_change
    enemyX += enemyX_change
    enemyY += enemyY_change
    enemy2X += enemy2X_change
    enemy2Y += enemy2Y_change
    enemy3X += enemy3X_change
    enemy3Y += enemy3Y_change
    enemy4X += enemy4X_change
    enemy4Y += enemy4Y_change
    enemy5X += enemy5X_change
    enemy5Y += enemy5Y_change

    #el jugador i els enemics en si
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    enemy2(enemy2X, enemy2Y)
    enemy3(enemy3X, enemy3Y)
    enemy4(enemy4X, enemy4Y)
    enemy5(enemy5X, enemy5Y)
    pygame.display.update()
