from core import *
import pygame as pg

try:
    import android
except ImportError:
    android = None

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,204,0)
TEXTCOLOR = GREEN
BGCOLOR = BLACK
BOXCOLOR = WHITE
color = {0:WHITE,2:(220,220,200),4:(220,150,150),8:(220,100,100),
        16:(220,50,50),32:(220,0,0),64:(150,30,30),128:(70,100,100),
        256:(70,150,150),512:(0,200,200),1024:(200,200,200)}
MOVECODE = {pg.K_LEFT:1,
            pg.K_UP:4,
            pg.K_DOWN:2, 
            pg.K_RIGHT:3}
def main():
    global font
    pg.init()
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)
    SCREEN_SIZE = (640,480)
    screen = pg.display.set_mode(SCREEN_SIZE,0,32)
    font = pg.font.SysFont("arial", 64)
    font_height = font.get_linesize()
    m = init()
    while True:
        moves=[]
        m_next = m
        for event in pg.event.get():
                if event.type == pg.KEYUP:
                    m_next,moves = next_map(m, MOVECODE[event.key])
                if event.type == pg.QUIT:
                    pg.quit()
        if still_alive(m_next)!="You Win!" and still_alive(m_next)!=False:
            #drawBoard(screen)
            drawTiles(m,m_next,moves,screen)
            pg.display.update()
            m=m_next
        elif still_alive(m_next)==False:
            screen.fill(BLACK)
            writeText('You Died!!', TEXTCOLOR, (320,200),screen)
            pg.display.update()
        elif still_alive(m_next)=="You Win!":
            screen.fill(BLACK)
            writeText('You Win!!', TEXTCOLOR, (320,200),screen)
            pg.display.update()

def drawBoard(screen):
    screen.fill(BLACK)
    for i in range(4):
        for j in range(4):
            pg.draw.rect(screen, WHITE, (120+100*i,40+100*j,90,90),0)
            #drawTile(screen,i,j,m[i][j])
def drawTiles(m, m_next, moves, screen):
    moves_original = []
    moves_target = []
    for move in moves:
        moves_original.append((move[0],move[1]))
        moves_target.append((move[2],move[3]))
    #moving process
    speed = 20
    for t in range(speed):
        drawBoard(screen)
        for i in range(4):
            for j in range(4):
                #if m[i][j]==m_next[i][j]: #static block
                 #   drawTile(screen,i,j,m[i][j],0,0)
                if (i,j) in moves_original:
                    index = moves_original.index((i,j))
                    drawTile(screen,i,j,m[i][j],
                    (moves_target[index][0]-moves_original[index][0])*100./float(speed)*t,
                    (moves_target[index][1]-moves_original[index][1])*100./float(speed)*t)
                else:
                    drawTile(screen,i,j,m[i][j],0,0)
        pg.display.update()
    #display new situation
    drawBoard(screen)
    for i in range(4):
        for j in range(4):
            drawTile(screen,i,j,m_next[i][j],0,0)
def drawTile(screen,i,j,number,adjx=0,adjy=0):
    left,top = 120+100*i,40+100*j
    pg.draw.rect(screen,color[number],(left+adjx,top+adjy,90,90),0)
    if number!=0:
        textSurf = font.render('%d'%number, True, TEXTCOLOR)
        textRect = textSurf.get_rect()
        textRect.center = left+adjx+45,top+adjy+45
        screen.blit(textSurf,textRect)

def writeText(text,color,center,screen):
    textSurf = font.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.center = center
    screen.blit(textSurf,textRect)

main()
