# Create a simple game using pygame

import pygame
import random
import math
from pygame import mixer


# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('files/images/background.png')

# Background sound
mixer.music.load('files/sounds/background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Copilot")
icon = pygame.image.load('files/images/copilot.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('files/images/player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

# Enemy
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('files/images/enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('files/images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# Ready
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
# Position of score
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Function to show score on screen
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 255))
    screen.blit(score, (x, y))

# Function to show game over text
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 255))
    screen.blit(over_text, (200, 250))

# Function to draw player on screen
def player(x, y):
    screen.blit(playerImg, (x, y))

# Function to draw enemy on screen
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Function to draw bullet on screen
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Function to check if bullet hit enemy
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) +
                         math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

# Game loop
running = True
while running:
    
        # RGB - Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background image
        screen.blit(background, (0, 0))
    
        # Check for events
        for event in pygame.event.get():
            # Check if user quit
            if event.type == pygame.QUIT:
                running = False
    
            # Check if key is pressed
            if event.type == pygame.KEYDOWN:
                # Check if key is left or right arrow
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
    
                # Check if key is spacebar
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        # Play bullet sound
                        bullet_sound = mixer.Sound('files/sounds/laser.mp3')
                        bullet_sound.play()
                        # Get current x coordinate of spaceship
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
    
            # Check if key is released
            if event.type == pygame.KEYUP:
                # Check if key is left or right arrow
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
    
        # Update player position
        playerX += playerX_change
    
        # Check if player is out of bounds
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736
    
        # Update enemy position
        for i in range(num_of_enemies):
    
            # Game over
            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    # Set enemy off screen
                    enemyY[j] = 2000
                game_over_text()
                break
    
            enemyX[i] += enemyX_change[i]
    
            # Check if enemy is out of bounds
            if enemyX[i] <= 0:
                enemyX_change[i] = 2
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -2
                enemyY[i] += enemyY_change[i]
    
            # Check for collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                # Play explosion sound
                explosion_sound = mixer.Sound('files/sounds/explosion.wav')
                explosion_sound.play()
                # Reset bullet
                bulletY = 480
                bullet_state = "ready"
                # Update score
                score_value += 1
                # Reset enemy
                enemyX[i] = random.randint(0, 735)
                enemyY[i] = random.randint(50, 150)

            # Draw enemy
            enemy(enemyX[i], enemyY[i], i)

        # Update bullet position
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        # Draw player
        player(playerX, playerY)
        # Draw score
        show_score(textX, textY)
        # Update screen
        pygame.display.update()

pygame.quit()