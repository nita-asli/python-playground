
import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 800
screen_height = 600

# Warna
white = (255, 255, 255)
black = (0, 0, 0)

# Karakter pemain
player_width = 50
player_height = 50
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10

# Objek yang jatuh
object_width = 50
object_height = 50

# Kecepatan objek jatuh
object_speed = 5

# Inisialisasi layar
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menangkap Benda")

# Fungsi untuk menggambar pemain
def draw_player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_width, player_height])

# Fungsi untuk menggambar objek jatuh
def draw_object(x, y):
    pygame.draw.rect(screen, white, [x, y, object_width, object_height])

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += 5

    # Gerakan objek jatuh
    object_y += object_speed
    if object_y > screen_height:
        object_y = 0
        object_x = random.randint(0, screen_width - object_width)

    # Deteksi tabrakan
    if (
        player_x < object_x + object_width
        and player_x + player_width > object_x
        and player_y < object_y + object_height
        and player_y + player_height > object_y
    ):
        print("Benda Ditangkap!")

    # Menggambar objek dan pemain
    screen.fill(black)
    draw_object(object_x, object_y)
    draw_player(player_x, player_y)

    pygame.display.flip()
    clock.tick(60)

