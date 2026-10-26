# library pygame dalam python
# untuk membuat game sederhana

# import dulu librarynya
import pygame

# inisiasi
pygame.init()

# buat tampilan window utamanya
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

# buat var untuk while loop
isRun = True

# buat objek gamenya
# koordinat
x = 250
y = 250
# panjang dan lebar objeknya
panjang = 20
lebar = 20
# kecepatan objeknya
speed = 10

# buat loop untuk menjalankan gamenya
while isRun:
    # membuat delay untuk gamenya
    pygame.time.delay(20)
    # menggunakan event dan menghentikan loop jika quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    # mengambil input dari user 
    key = pygame.key.get_pressed()

    # jika user mengarahkan ke kiri
    if key[pygame.K_LEFT] and x > 0:
        x -= speed
    # jika user mengarahkan ke kanan
    if key[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed
    # jika user mengarahkan ke bawah
    if key[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed
    # jika user mengarahkan ke atas
    if key[pygame.K_UP] and y > 0:
        y -= speed
    
    # mengubah warna window
    window.fill((255,255,255))
    # menggambar objek di dalam window
    pygame.draw.rect(window,(255,0,0),(x,y,lebar,panjang))
    # mengupdate display game
    pygame.display.update()

# quit dari game
pygame.quit()