import contextlib
with contextlib.redirect_stdout(None) :
    import pygame
from pygame.locals import *
from random import *

def affich() :
    if ecran == 1 :
        pygame.draw.rect(fenetre,(0,0,0),(0,0,600,600))
        myfont = pygame.font.SysFont("Courier New",96)
        texte = myfont.render("TETRIS",False,(170,20,170))
        fenetre.blit(texte,(130,200))
        myfont = pygame.font.SysFont("Courier New",24)
        texte = myfont.render("> PUSH RETURN",False,(255,255,255))
        fenetre.blit(texte,(200,400))
        myfont = pygame.font.SysFont("Courier New",12)
        texte = myfont.render("Aide (a)",False,(255,255,255))
        fenetre.blit(texte,(5,580))
        if aide == 1 :
            texte = myfont.render("Commandes :",False,(255,255,255))
            fenetre.blit(texte,(5,5))
            texte = myfont.render("< : Déplacer la pièce vers la gauche",False,(255,255,255))
            fenetre.blit(texte,(5,20))
            texte = myfont.render("> : Déplacer la pièce vers la droite",False,(255,255,255))
            fenetre.blit(texte,(5,35))
            texte = myfont.render("v : Faire tomber la pièce plus vite",False,(255,255,255))
            fenetre.blit(texte,(5,50))
            texte = myfont.render("a/espace/^ : Faire tourner la pièce vers la gauche",False,(255,255,255))
            fenetre.blit(texte,(5,65))
            texte = myfont.render("z : Faire tourner la pièce vers la droite",False,(255,255,255))
            fenetre.blit(texte,(5,80))
    elif ecran == 2 :
        myfont = pygame.font.SysFont("Courier",24)

        pygame.draw.rect(fenetre,(55,55,55),(0,0,600,600))

        pygame.draw.rect(fenetre,(255,255,255),(173,28,254,29))
        pygame.draw.rect(fenetre,(0,0,0),(175,30,250,25))
        texte = myfont.render("LINES - "+str(statistiques[3]),False,(255,255,255))
        fenetre.blit(texte,(180,30))

        pygame.draw.rect(fenetre,(255,255,255),(438,28,134,124))
        pygame.draw.rect(fenetre,(0,0,0),(440,30,130,120))
        texte = myfont.render("TOP :",False,(255,255,255))
        fenetre.blit(texte,(445,30))
        texte = myfont.render(str(statistiques[1]),False,(255,255,255))
        fenetre.blit(texte,(445,60))
        texte = myfont.render("SCORE :",False,(255,255,255))
        fenetre.blit(texte,(445,90))
        texte = myfont.render(str(statistiques[2]),False,(255,255,255))
        fenetre.blit(texte,(445,120))

        pygame.draw.rect(fenetre,(255,255,255),(438,163,134,144))
        pygame.draw.rect(fenetre,(0,0,0),(440,165,130,140))
        texte = myfont.render("NEXT :",False,(255,255,255))
        fenetre.blit(texte,(445,165))
        for i in range (4) :
            for j in range (4) :
                if piece_annonce[i][j] == 1 :
                    pygame.draw.rect(fenetre,(0,0,0),(455+j*25,195+i*25,25,25))
                    pygame.draw.rect(fenetre,(piece_annonce[5],piece_annonce[6],piece_annonce[7]),(457+j*25,197+i*25,21,21))

        pygame.draw.rect(fenetre,(255,255,255),(438,318,134,64))
        pygame.draw.rect(fenetre,(0,0,0),(440,320,130,60))
        texte = myfont.render("LEVEL :",False,(255,255,255))
        fenetre.blit(texte,(445,320))
        texte = myfont.render(str(statistiques[0]),False,(255,255,255))
        fenetre.blit(texte,(445,350))

        pygame.draw.rect(fenetre,(255,255,255),(28,28,134,370))
        pygame.draw.rect(fenetre,(0,0,0),(30,30,130,366))
        texte = myfont.render("STATS :",False,(255,255,255))
        fenetre.blit(texte,(35,30))
        for i in range (7) :
            for j in range (4) :
                for k in range (4) :
                    if figures[i][j][k] == 1 :
                        if i == 0 :
                            c = (190,30,30)
                        elif i == 1 :
                            c = (240,210,30)
                        elif i == 2 :
                            c = (255,130,15)
                        elif i == 3 :
                            c = (50,190,220)
                        elif i == 4 :
                            c = (40,50,190)
                        elif i == 5 :
                            c = (140,50,140)
                        elif i == 6 :
                            c = (40,140,30)
                        pygame.draw.rect(fenetre,(0,0,0),(35+k*12,60+j*12+i*48,12,12))
                        pygame.draw.rect(fenetre,c,(36+k*12,61+j*12+i*48,10,10))
        for i in range (7) :
            texte = myfont.render(str(statistiques[i+4]),False,(255,255,255))
            fenetre.blit(texte,(98,69+i*48))

        pygame.draw.rect(fenetre,(255,255,255),(173,68,254,504))
        pygame.draw.rect(fenetre,couleurs[statistiques[0]][0],(175,70,250,500))
        for i in range (5) :
            pygame.draw.rect(fenetre,couleurs[statistiques[0]][1],(200+i*25+(i-1)*25,70,25,500))

        for i in range (20) :
            for j in range (10) :
                if not grille[i*10+j] == (0,0,0) :
                    pygame.draw.rect(fenetre,(0,0,0),(175+j*25,70+i*25,25,25))
                    pygame.draw.rect(fenetre,grille[i*10+j],(177+j*25,72+i*25,21,21))
        for i in range (4) :
            for j in range (4) :
                if piece[i][j] == 1 and y+i >= 0 :
                    pygame.draw.rect(fenetre,(0,0,0),(175+(x+j)*25,70+(y+i)*25,25,25))
                    pygame.draw.rect(fenetre,(piece[5],piece[6],piece[7]),(177+(x+j)*25,72+(y+i)*25,21,21))

    elif ecran == 3 :
        pygame.draw.rect(fenetre,(0,0,0),(0,0,600,600))
        myfont = pygame.font.SysFont("Courier",24)
        texte = myfont.render("PAUSE",False,(255,255,255))
        fenetre.blit(texte,(265,285))

    pygame.display.flip()

def change_piece() :
    global ecran
    global piece
    global piece_annonce
    global statistiques
    global x
    global y
    x = 3
    y = -1
    piece = piece_annonce
    alea = randint(0,6)
    piece_annonce = figures[alea]
    piece_annonce += [alea]
    if alea == 0 :
        piece_annonce += [190,30,30]
    elif alea == 1 :
        piece_annonce += [240,210,30]
    elif alea == 2 :
        piece_annonce += [255,130,15]
    elif alea == 3 :
        piece_annonce += [50,190,220]
    elif alea == 4 :
        piece_annonce += [40,50,190]
    elif alea == 5 :
        piece_annonce += [140,50,140]
    elif alea == 6 :
        piece_annonce += [40,140,30]
    non = 0
    for i in range (4) :
        for j in range (4) :
            if piece[i][j] == 1 and not grille[(y+i)*10+x+j] == (0,0,0) :
                non = 1
                break
        if non == 1 :
            break
    if non == 1 :
        affich()
        pygame.time.wait(1000)
        ecran = 4
        if statistiques[2] > statistiques[1] :
            statistiques[1] = statistiques[2]
        myfont = pygame.font.SysFont("Courier New",24)
        texte = myfont.render("> PUSH RETURN TO RESTART",False,(255,255,255))
        fenetre.blit(texte,(125,572))
        affich()

def down() :
    global grille
    global y
    global piece
    non = 0
    for i in range (4) :
        for j in range (3,-1,-1) :
            if piece[j][i] == 1 :
                if not y+5-(4-j) == 20 :
                    if not grille[(y+5-(4-j))*10+x+i] == (0,0,0) :
                        non = 1
                    break
                else :
                    non = 1
                    break
        if non == 1 :
            for i in range (4) :
                for j in range (4) :
                    if piece[i][j] == 1 and y+i >= 0 :
                        grille[(y+i)*10+x+j] = (piece[5],piece[6],piece[7])
            statistiques[piece[4]+4] += 1
            piece = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],0,0,0,0]
            del_lignes()
            change_piece()
            break
    if non == 0 :
        y += 1

def left() :
    global grille
    global x
    non = 0
    for i in range (4) :
        for j in range (4) :
            if piece[i][j] == 1 :
                if not x-1+j == -1 :
                    if not grille[(y+i)*10+x-1+j] == (0,0,0) :
                        non = 1
                    break
                else :
                    non = 1
                    break
    if non == 0 :
        x -= 1

def right() :
    global grille
    global x
    non = 0
    for i in range (4) :
        for j in range (3,-1,-1) :
            if piece[i][j] == 1 :
                if not x+5-(4-j) == 10 :
                    if not grille[(y+i)*10+x+5-(4-j)] == (0,0,0) :
                        non = 1
                    break
                else :
                    non = 1
                    break
    if non == 0 :
        x += 1

def turn_left() :
    global piece
    p = []
    for i in range (3,-1,-1) :
        p += [[piece[0][i],piece[1][i],piece[2][i],piece[3][i]]]
    non = 0
    for i in range (4) :
        for j in range (4) :
            if p[i][j] == 1 :
                if x+j < 0 or x+j > 9 or y+i > 19 or not grille[(y+i)*10+x+j] == (0,0,0) :
                    non = 1
                    break
        if non == 1 :
            break
    if non == 0 :
        piece = p+[piece[4],piece[5],piece[6],piece[7]]

def turn_right() :
    global piece
    p = []
    for i in range (4) :
        p += [[piece[3][i],piece[2][i],piece[1][i],piece[0][i]]]
    non = 0
    for i in range (4) :
        for j in range (4) :
            if p[i][j] == 1 :
                if x+j < 0 or x+j > 9 or y+i > 19 or not grille[(y+i)*10+x+j] == (0,0,0) :
                    non = 1
                    break
        if non == 1 :
            break
    if non == 0 :
        piece = p+[piece[4],piece[5],piece[6],piece[7]]

def del_lignes() :
    global grille
    global statistiques
    l = []
    for i in range (20) :
        non = 0
        for j in range (10) :
            if grille[i*10+j] == (0,0,0) :
                non = 1
                break
        if non == 0 :
            l += [i]
    total = len(l)
    for i in range (len(l)) :
        grille = grille[0:l[0]*10]+[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]+grille[l[0]*10+10:len(grille)]
        affich()
        pygame.time.wait(200)
        del grille[l[0]*10:l[0]*10+10]
        grille = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]+grille
        affich()
        pygame.time.wait(200)
        del l[0]
    statistiques[3] += total
    if total == 1 :
        total = 10
    elif total == 2 :
        total = 100
    elif total == 3 :
        total = 500
    elif total == 4 :
        total = 1000
    statistiques[2] += total*(statistiques[0]+1)

    if statistiques[2] >= 50000 :
        statistiques[0] = 5
    elif statistiques[2] >= 20000 :
        statistiques[0] = 4
    elif statistiques[2] >= 10000 :
        statistiques[0] = 3
    elif statistiques[2] >= 5000 :
        statistiques[0] = 2
    elif statistiques[2] >= 1000 :
        statistiques[0] = 1

pygame.init()

fenetre = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tetris")

raccourci = __file__
raccourci = raccourci[0:-8]

icone = pygame.image.load(raccourci+"icone.png")
pygame.display.set_icon(icone)

statistiques = [0,0,0,0,0,0,0,0,0,0,0]
figures = [[[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[1,1,1,0],[1,0,0,0],[0,0,0,0]],[[0,0,0,0],[1,1,1,0],[0,0,1,0],[0,0,0,0]],[[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]],[[0,0,0,0],[1,1,1,0],[0,1,0,0],[0,0,0,0]],[[0,0,0,0],[0,1,1,0],[1,1,0,0],[0,0,0,0]],[[0,0,0,0],[1,1,0,0],[0,1,1,0],[0,0,0,0]]]
couleurs = [[(0,0,255),(0,0,128)],[(0,255,255),(0,128,128)],[(0,255,0),(0,128,0)],[(255,255,0),(128,128,0)],[(255,0,0),(128,0,0)],[(0,0,0),(255,255,255)]]
ecran = 1
appuie = 0
aide = 0

affich()

pygame.key.set_repeat(300,100)

b = 1
while b == 1 :
    for event in pygame.event.get() :
        if event.type == QUIT :
            b = 0
            pygame.quit()

        elif event.type == KEYDOWN :
            if event.key == K_RETURN :
                if ecran == 1 or ecran == 4 :
                    ecran = 2
                    t = 0
                    grille = []
                    for i in range (200) :
                        grille += [(0,0,0)]
                    statistiques = [0,statistiques[1],0,0,0,0,0,0,0,0,0]
                    alea = randint(0,6)
                    piece_annonce = figures[alea]
                    piece_annonce += [alea]
                    if alea == 0 :
                        piece_annonce += (190,30,30)
                    elif alea == 1 :
                        piece_annonce += (240,210,30)
                    elif alea == 2 :
                        piece_annonce += (255,130,15)
                    elif alea == 3 :
                        piece_annonce += (50,190,220)
                    elif alea == 4 :
                        piece_annonce += (40,50,190)
                    elif alea == 5 :
                        piece_annonce += (140,50,140)
                    elif alea == 6 :
                        piece_annonce += (40,140,30)
                    change_piece()
                elif ecran == 2 :
                    ecran = 3
                elif ecran == 3 :
                    ecran = 2

            elif event.key == K_DOWN :
                appuie = 1
                down()
            elif event.key == K_LEFT :
                left()
            elif event.key == K_RIGHT :
                right()
            elif event.key == K_q and ecran == 1 :
                if aide == 0 :
                    aide = 1
                else :
                    aide = 0
            elif event.key == K_q or event.key == K_SPACE or event.key == K_UP :
                turn_left()
            elif event.key == K_w :
                turn_right()

            affich()

        elif event.type == KEYUP :
            if event.key == K_DOWN :
                appuie = 0

    if ecran == 2 and appuie == 0 :
        t += 1
        pygame.time.wait(1)
        if t > 600-statistiques[0]*100 :
            t = 0
            down()
            affich()