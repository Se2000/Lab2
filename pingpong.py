import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 30
fpsZegar = pygame.time.Clock()
OKNOGRY_SZER = 800
OKNOGRY_WYS = 400

OKNOGRY = pygame.display.set_mode((OKNOGRY_SZER,OKNOGRY_WYS), 0, 32)
pygame.display.set_caption('Prosty Pong')
LT_BLUE = (230, 255, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PALETKA_SZER = 100
PALETKA_WYS = 20
PALETKA_1_POZ = (350, 360) # początkowa pozycja paletki gracza
paletka1_obr = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletka1_obr.fill(BLUE)
paletka1_prost = paletka1_obr.get_rect()
paletka1_prost.x = PALETKA_1_POZ[0]
paletka1_prost.y = PALETKA_1_POZ[1]

AI_PREDKOSC = 3

PILKA_SZER = 20
PILKA_WYS = 20
PILKA_PREDKOSC_X = 6
PILKA_PREDKOSC_Y = 6
pilka_obr = pygame.Surface([PILKA_SZER, PILKA_WYS], pygame.SRCALPHA,32).convert_alpha()
pygame.draw.ellipse(pilka_obr, GREEN, [0, 0, PILKA_SZER, PILKA_WYS])
pilka_prost = pilka_obr.get_rect()
pilka_prost.x = OKNOGRY_SZER/2
pilka_prost.y = OKNOGRY_WYS/2

GRACZ_1_PKT = '0'
GRACZ_2_PKT = '0'
# fontObj = pygame.font.Font('pingpong.ttf', 64)
fontObj = pygame.font.SysFont('arial', 20)

def drukuj_punkty_p1():
    tekst_obr1 = fontObj.render(GRACZ_1_PKT, True, (0,0,0))
    tekst_prost1 = tekst_obr1.get_rect()
    tekst_prost1.center = (OKNOGRY_SZER/2, OKNOGRY_WYS*0.75)
    OKNOGRY.blit(tekst_obr1, tekst_prost1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if event.type == MOUSEMOTION:
        myszaX, myszaY = event.pos

przesuniecie = myszaX-(PALETKA_SZER/2)
if przesuniecie > OKNOGRY_SZER-PALETKA_SZER:
    przesuniecie = OKNOGRY_SZER-PALETKA_SZER
if przesuniecie < 0:
    przesuniecie = 0
paletka1_prost.x = przesuniecie

if pilka_prost.centerx > paletka2_prost.centerx:
    paletka2_prost.x += AI_PREDKOSC
elif pilka_prost.centerx <paletka2_prost.centerx:
    paletka2_prost.x -= AI_PREDKOSC
pilka_prost.x += PILKA_PREDKOSC_X
pilka_prost.y += PILKA_PREDKOSC_Y

if pilka_prost.right >= OKNOGRY_SZER:
    PILKA_PREDKOSC_X *= -1
if pilka_prost.left <= 0:
    PILKA_PREDKOSC_X *= -1

if pilka_prost.colliderect(paletka1_prost):
    PILKA_PREDKOSC_Y *= -1
    pilka_prost.bottom = paletka1_prost.top
if pilka_prost.colliderect(paletka2_prost):
    PILKA_PREDKOSC_Y *= -1
    pilka_prost.top = paletka2_prost.bottom

if pilka_prost.top <= 0:
    pilka_prost.x = OKNOGRY_SZER/2
    pilka_prost.y = OKNOGRY_WYS/2
    GRACZ_1_PKT = str(int(GRACZ_1_PKT)+1)
if pilka_prost.bottom >= OKNOGRY_WYS:
    pilka_prost.x = OKNOGRY_SZER/2
    pilka_prost.y = OKNOGRY_WYS/2
    GRACZ_2_PKT = str(int(GRACZ_2_PKT)+1)

OKNOGRY.fill(LT_BLUE)
drukuj_punkty_p1()
drukuj_punkty_p2()
OKNOGRY.blit(paletka1_obr, paletka1_prost)
OKNOGRY.blit(paletka2_obr, paletka2_prost)
OKNOGRY.blit(pilka_obr, pilka_prost)
pygame.display.update()
fpsZegar.tick(FPS)



