import pygame
import random

#initialization of pygame
pygame.init()

#screen display
screen = pygame.display.set_mode((320,700))

#icon
pygame.display.set_caption("RadishPiano 1.0")
icon = pygame.image.load("assets/visuals/grand-piano.png")
pygame.display.set_icon(icon)

#background
background = pygame.image.load('assets/visuals/bucket.png')

#number of tiles
n = 99999

#tiles
blueImg = pygame.image.load('assets/visuals/radish.png')
tileImg1 = blueImg
tileImg2 = blueImg
tileImg3 = blueImg
tileImg4 = blueImg
tileImg5 = blueImg

tileY_change = 5

blackImg = pygame.image.load('assets/visuals/blank.png')

#sound
piano = [pygame.mixer.Sound('assets/audio/piano1.mp3'), pygame.mixer.Sound('assets/audio/piano2.mp3'),
         pygame.mixer.Sound('assets/audio/piano3.mp3'), pygame.mixer.Sound('assets/audio/piano4.mp3'),
         pygame.mixer.Sound('assets/audio/piano5.mp3'), pygame.mixer.Sound('assets/audio/piano6.mp3'),
         pygame.mixer.Sound('assets/audio/piano7.mp3')]

#border
border2 = pygame.Rect(0, 550, 340, 5)


Ya1 = -180
Xa1 = 0
Ya2 = -360
Xa2 = -900
Ya3 = -720
Xa3 = -900
Ya4 = -10000
Xa4 = -10000
Ya5 = -10000
Xa5 = -10000



lst_tiles = []
lst_order = []

for i in range(n):
    lst_tiles.append(random.randint(1,4))
for i in range(len(lst_tiles)-1):
    if lst_tiles[i] == 1:
        lst_tiles[i] = 0
        
    elif lst_tiles[i] == 2:
        lst_tiles[i] = 70

    elif lst_tiles[i] == 3:
        lst_tiles[i] = 140

    elif lst_tiles[i] == 4:
        lst_tiles[i] = 210


def Y_tiles(tileY):
    tileY = tileY + tileY_change

def tiles(x,y, tileImg):
    screen.blit(tileImg, (x, y))
    
def game_over():
    over_font = pygame.font.Font('freesansbold.ttf', 45)
    over_text = over_font.render("GAME OVER!", True, (54, 100, 139, 255))
    screen.blit(over_text, (15, 150))
    pygame.display.update()
    pygame.time.delay(5000)

running = True
clock = pygame.time.Clock()
block1 = 0
block2 = 0
block3 = 0
block4 = 0

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        piano_i = random.randint(0,6)
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
        
            if Ya1 >= 400 and Ya1 <= 555:
                if Xa1 == 0:
                    if event.key == pygame.K_a:
                        piano[piano_i].play()
                        tileImg1 = blackImg
                        block1 += 1
                    if event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                        
                elif Xa1 == 70:
                    if event.key == pygame.K_s:
                        piano[piano_i].play()
                        tileImg1 = blackImg
                        block2 += 1
                    if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                        
                elif Xa1 == 140:
                    if event.key == pygame.K_d:
                        piano[piano_i].play()
                        tileImg1 = blackImg
                        block3 +=1
                    if event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                        
                elif Xa1 == 210:
                    if event.key == pygame.K_f:
                        piano[piano_i].play()
                        tileImg1 = blackImg
                        block4 += 1
                    if event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_a:
                        game_over()
                        running = False
                        break
                    
            if Ya2 >= 400 and Ya2 <= 550:
                if Xa2 == 0:
                    if event.key == pygame.K_a:
                        tileImg2 = blackImg
                        piano[piano_i].play()
                        block1 += 1
                    if event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                        
                elif Xa2 == 70:
                    if event.key == pygame.K_s:
                        tileImg2 = blackImg
                        piano[piano_i].play()
                        block2 += 1

                    if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                        
                elif Xa2 == 140:
                    if event.key == pygame.K_d:
                        tileImg2 = blackImg
                        piano[piano_i].play()
                        block3 +=1
                    if event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                        
                elif Xa2 == 210:
                    if event.key == pygame.K_f:
                        tileImg2 = blackImg
                        piano[piano_i].play()
                        block4 += 1
                    if event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_a:
                        game_over()
                        running = False
                        break
                                        
            if Ya3 >= 400 and Ya3 <= 550:
                if Xa3 == 0:
                    if event.key == pygame.K_a:
                        tileImg3 = blackImg
                        piano[piano_i].play()
                        block1 += 1
                    if event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                                            
                elif Xa3 == 70:
                    if event.key == pygame.K_s:
                        tileImg3 = blackImg
                        piano[piano_i].play()
                        block2 += 1
                    if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                                            
                elif Xa3 == 140:
                    if event.key == pygame.K_d:
                        tileImg3 = blackImg
                        piano[piano_i].play()
                        block3 +=1
                    if event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                                            
                elif Xa3 == 210:
                    if event.key == pygame.K_f:
                        tileImg3 = blackImg
                        piano[piano_i].play()
                        block4 += 1
                    if event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_a:
                        game_over()
                        running = False
                        break
                                        
            if Ya4 >= 400 and Ya4 <= 550:
                if Xa4 == 0:
                    if event.key == pygame.K_a:
                        tileImg4 = blackImg
                        piano[piano_i].play()
                        block1 += 1
                    if event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                                            
                elif Xa4 == 70:
                    if event.key == pygame.K_s:
                        tileImg4 = blackImg
                        piano[piano_i].play()
                        block2 += 1
                    if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                                            
                elif Xa4 == 140:
                    if event.key == pygame.K_d:
                        tileImg4 = blackImg
                        piano[piano_i].play()
                        block3 +=1
                    if event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                                            
                elif Xa4 == 210:
                    if event.key == pygame.K_f:
                        tileImg4 = blackImg
                        piano[piano_i].play()
                        block4 += 1
                    if event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_a:
                        game_over()
                        running = False
                        break
                                        
            if Ya5 >= 400 and Ya5 <= 550:
                if Xa5 == 0:
                    if event.key == pygame.K_a:
                        tileImg5 = blackImg
                        piano[piano_i].play()
                        block1 += 1
                    if event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                                            
                elif Xa5 == 70:
                    if event.key == pygame.K_s:
                        tileImg5 = blackImg
                        piano[piano_i].play()
                        block2 += 1
                    if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break            
                                    
                elif Xa5 == 140:
                    if event.key == pygame.K_d:
                        tileImg5 = blackImg
                        piano[piano_i].play()
                        block3 +=1
                    if event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_f:
                        game_over()
                        running = False
                        break
                                            
                elif Xa5 == 210:
                    if event.key == pygame.K_f:
                        tileImg5 = blackImg
                        piano[piano_i].play()
                        block4 += 1

                    if event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_a:
                        game_over()
                        running = False
                        break
                    
            if Ya1 > 325 and Ya1 < 400 or Ya2 > 325 and Ya2 < 400 or Ya3 > 325 and Ya3 < 400 or Ya4 > 325 and Ya4 < 400 or Ya5 > 325 and Ya5 < 400:
                if event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_f:
                    
                    game_over()
                    
                    running = False
                    break
    
    if Ya1 == 0:
        Ya2 = -230
        Xa2 = lst_tiles.pop(0)
        tileImg2 = blueImg
        
    if Ya2 == 0:
        Ya3 = -230
        Xa3 = lst_tiles.pop(0)
        tileImg3 = blueImg
        
    if Ya3 == 0:
        Ya4 = -230
        Xa4 = lst_tiles.pop(0)
        tileImg4 = blueImg
        
    if Ya4 == 0:
        Ya5 = -230
        Xa5 = lst_tiles.pop(0)
        tileImg5 = blueImg
        
    if Ya5 == 0:
        Ya1 = -230
        Xa1 = lst_tiles.pop(0)
        tileImg1 = blueImg
    
    
    
    
    Ya1 = Ya1 + tileY_change
    Ya2 = Ya2 + tileY_change
    Ya3 = Ya3 + tileY_change
    Ya4 = Ya4 + tileY_change
    Ya5 = Ya5 + tileY_change
    
    
    
    tiles(Xa1, Ya1, tileImg1)
    tiles(Xa2, Ya2, tileImg2)
    tiles(Xa3, Ya3, tileImg3)
    tiles(Xa4, Ya4, tileImg4)
    tiles(Xa5, Ya5, tileImg5)

    

    tilespersecond = 30/28.6
    seconds = int(pygame.time.get_ticks()) /1000 -2.18
    realscore =  tilespersecond * seconds

    score = block1 + block2+ block3 + block4 
    if score > realscore + 3 or score < realscore - 5:
        game_over()
        
        running = False
        
        print(score,realscore)


    pygame.draw.rect(screen, (224, 255, 255, 255), border2)
    
    pygame.display.update()
