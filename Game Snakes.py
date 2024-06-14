import pygame, random, os, tkinter


# ARROW - PLAYER 1
# WASD - PLAYER 2

x = pygame.init()
root = tkinter.Tk()
pcspecs = (root.winfo_screenwidth(),root.winfo_screenheight())
           
pygame.mixer.init()
snah, snaw = 30, 30
snahh, snaww = 30, 30

pygame.font.get_fonts()
font = pygame.font.SysFont('arialblue', 60)

def tex(text, greenor, x, y) : 
    screen_text = font.render(text, True, greenor)
    win.blit(screen_text, [x,y])


def plot(win, snake1_list, img) :
    a = 0
    b = 0
    for x,y in snake1_list : 
        if a != 0 and b != 0 :
            win.blit(img, (x,y))
        a += 1
        b += 1

# BASIC SETTING 
win = pygame.display.set_mode(pcspecs, pygame.FULLSCREEN)
pygame.display.set_caption("Something, I don't know")
pygame.display.update()
clock = pygame.time.Clock()

# IMAGE SETUP
bg = pygame.transform.scale(pygame.image.load("images/grass.gif"), (pcspecs[0], pcspecs[1])).convert_alpha()
bground = pygame.transform.scale(pygame.image.load("images/image.jpg"), (pcspecs[0], pcspecs[1])).convert_alpha()
start = pygame.transform.scale(pygame.image.load("images/title.png"), (pcspecs[0]/1.7, pcspecs[1]/9)).convert_alpha()
vol = pygame.transform.scale(pygame.image.load("images/vol.png"), (pcspecs[0]/34, pcspecs[1]/18)).convert_alpha()
novol = pygame.transform.scale(pygame.image.load("images/novol.png"), (pcspecs[0]/34, pcspecs[1]/18)).convert_alpha()
score1 = pygame.transform.scale(pygame.image.load("images/score1.png"), (30, 30)).convert_alpha()
borderimg = pygame.transform.scale(pygame.image.load("images/gradient.jpeg"), (pcspecs[0], pcspecs[1]/14.4)).convert_alpha()
foodimg = pygame.transform.scale(pygame.image.load("images/apple.png"), (30, 30)).convert_alpha()
score1img = pygame.transform.scale(pygame.image.load("images/score1.png"), (pcspecs[0]/8,pcspecs[1]/30)).convert_alpha()
colonimg = pygame.transform.scale(pygame.image.load("images/colon.png"), (10, 20)).convert_alpha()
hscore = pygame.transform.scale(pygame.image.load("images/highscore.png"), (pcspecs[0]/6.8,pcspecs[1]/30)).convert_alpha()
gover = pygame.transform.scale(pygame.image.load("images/over.png"), (650,90)).convert_alpha() 
blimg = pygame.transform.scale(pygame.image.load("images/blur.png") , (pcspecs[0], pcspecs[1])).convert_alpha()
resetimg = pygame.transform.scale(pygame.image.load("images/reset.png") , (pcspecs[0]/2,pcspecs[1]/30)).convert_alpha()
menuimg = pygame.transform.scale(pygame.image.load("images/menu.png") , (pcspecs[0]/2,pcspecs[1]/30)).convert_alpha()

defvol = True                   # Volume button boolean

def loadscreen() : 
    exit_game = False 
    play1text = pygame.transform.scale(pygame.image.load("images/playbutton1.png"), (pcspecs[0]/6.8,pcspecs[1]/35)).convert_alpha()
    play2text = pygame.transform.scale(pygame.image.load("images/playbutton2.png"), (pcspecs[0]/6.8,pcspecs[1]/35)).convert_alpha()
    but1dim = (pcspecs[0]//3-10, pcspecs[1]//3)
    but2dim = (but1dim[0], pcspecs[1]//3+100)
    but3dim = (pcspecs[0]//2-20, 2*pcspecs[1]//3-50)
    button1_rect = pygame.Rect(but1dim[0], but1dim[1], pcspecs[0]/3, pcspecs[1]/18)
    button2_rect = pygame.Rect(but2dim[0], but2dim[1], pcspecs[0]/3, pcspecs[1]/18)
    button3_rect = pygame.Rect(but3dim[0], but3dim[1], pcspecs[0]/27, pcspecs[1]/14.5)
    pygame.mixer.music.load("music/game sound3.mp3")
    global defvol
    pygame.mixer.music.play()
    while not exit_game : 
        win.blit(bg, (0,0))
        win.blit(start, (pcspecs[0]//5, pcspecs[1]/7.2))
        pygame.draw.rect(win, (0,0,0), button1_rect)
        pygame.draw.rect(win, (0,0,0), button2_rect)
        pygame.draw.rect(win, (255,255,255), button3_rect)
        win.blit(play1text, (but1dim[0]+(but1dim[0]/3-10), but1dim[1]+10))
        win.blit(play2text, (but2dim[0]+(but2dim[0]/3-10), but2dim[1]+10))

        if defvol:
            win.blit(vol, (but3dim[0]+5, but3dim[1]+5))
            pygame.mixer.music.unpause()
        else:
            win.blit(novol, (but3dim[0]+5, but3dim[1]+5))
            pygame.mixer.music.pause()

        # BUTTON FUNCTIONALITY
        pygame.time.delay(100)
        for event in pygame.event.get():
            mloc = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if button3_rect.collidepoint(mloc):
                    defvol = not defvol
                elif button1_rect.collidepoint(mloc) :
                    gameloop1()
                elif button2_rect.collidepoint(mloc): 
                    gameloop2()
            if event.type == pygame.KEYDOWN : 
                if event.key == pygame.K_ESCAPE : 
                    quit()

        pygame.display.update()
        clock.tick(60)

def gameloop1() :
    # PLAYER 1 SPRITES
    direction1= "LEFT"
    p1sleft = pygame.transform.scale(pygame.image.load("images/p2 left.png"), (30, 30)).convert_alpha()
    p1sright = pygame.transform.scale(pygame.image.load("images/p2 right.png"), (30, 30)).convert_alpha()
    p1sup = pygame.transform.scale(pygame.image.load("images/p2 up.png"), (30, 30)).convert_alpha()
    p1sdown = pygame.transform.scale(pygame.image.load("images/p2 down.png"), (30, 30)).convert_alpha()
    p1sbody = pygame.transform.scale(pygame.image.load("images/p2 body.png"), (30, 30)).convert_alpha()
    p1s = p1sleft

    global defvol
    if defvol :
        pygame.mixer.music.load("music/ingame music3.mp3")
        pygame.mixer.music.play()

    snax, snay = pcspecs[0]/2, pcspecs[1]/2
    velx = 0 
    vely = 0
    foodx = random.randint(0, 1300)
    foody = random.randint(50, 700)
    score1 = 0 
    exit_game = False 
    game_over = False 
    snake1_list = []
    snake1_length = 1
    wloc, hloc = [x for x in range(10, 1340, 10)], [x for x in range(55, 746, 10)]


    if(not os.path.exists("data/highscore.txt")) : 
      with open("data/highscore.txt", "w") as b : 
        b.write("0")
    with open("data/highscore.txt", "r") as f :
        high = f.read()
    
    while not exit_game :
        if game_over : 
            win.blit(gover, (360,120))
            win.blit(blimg, (0,53))
            win.blit(resetimg, (pcspecs[0]/4, 1.5*pcspecs[1]/3))
            win.blit(menuimg, ((pcspecs[0]/4, 1.8*pcspecs[1]/3)))
            with open("data/highscore.txt", "w") as t: 
                t.write(str(high))     
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    exit_game = True
                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_RETURN : 
                        gameloop1()  
                    if event.key == pygame.K_ESCAPE : 
                        loadscreen()
        else : 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loadscreen()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and direction1 != "LEFT":
                        velx = 10
                        vely = 0
                        direction1 = "RIGHT"
                    elif event.key == pygame.K_LEFT and direction1 != "RIGHT":
                        velx = -10
                        vely = 0
                        direction1 = "LEFT"
                    elif event.key == pygame.K_UP and direction1 != "DOWN":
                        vely = -10
                        velx = 0
                        direction1 = "UP"
                    elif event.key == pygame.K_DOWN and direction1 != "UP":
                        vely = 10
                        velx = 0
                        direction1 = "DOWN"

            snax = snax + velx
            snay = snay + vely
            if direction1 == "RIGHT":
                p1s = p1sright
            elif direction1 == "LEFT":
                p1s = p1sleft
            elif direction1 == "UP":
                p1s = p1sup
            elif direction1 == "DOWN":
                p1s = p1sdown

            foodsound = pygame.mixer.Sound("music/foodsound.mp3")
            foodsound.set_volume(0.5)
            if abs(snax - foodx) < 30 and abs(snay - foody) < 30 : 
                foodsound.play(0)
                score1 += 1 
                foodx = random.choice(wloc)
                foody = random.choice(hloc)
                snake1_length += 2

            win.blit(bground, (0,0))
            win.blit(foodimg, (foodx, foody))
            win.blit(borderimg, (0, 0))        
            win.blit(score1img, (pcspecs[0]/3+150, pcspecs[1]/45))
            win.blit(colonimg, (pcspecs[0]/3+330, pcspecs[1]/45))
            tex(str(score1), (0, 0, 0), pcspecs[0]/3+350, pcspecs[1]/75)
            win.blit(hscore, (20, pcspecs[1]/45))
            win.blit(colonimg, (230, pcspecs[1]/45))
            tex(str(high), (0, 0, 0), 250, pcspecs[1]/75)
            if int(high) < score1 : 
                high = score1

            head1 = []
            head1.append(snax)
            head1.append(snay)    
            snake1_list.append(head1)

            if len(snake1_list) > snake1_length : 
                del snake1_list[0]
            if snax < 0 or snax > pcspecs[0]-30 or snay > pcspecs[1] or abs(snay-pcspecs[1]/14.4)<5 or head1 in snake1_list[:-1]: 
                game_over = True
            
            plot(win, snake1_list, p1sbody)
            win.blit(p1s, tuple(snake1_list[-1]))

        pygame.display.update()
        clock.tick(30)



def gameloop2() : 
    # PLAYER 1 SPRITES
    direction1= "LEFT"
    p1sleft = pygame.transform.scale(pygame.image.load("images/p2 left.png"), (30, 30)).convert_alpha()
    p1sright = pygame.transform.scale(pygame.image.load("images/p2 right.png"), (30, 30)).convert_alpha()
    p1sup = pygame.transform.scale(pygame.image.load("images/p2 up.png"), (30, 30)).convert_alpha()
    p1sdown = pygame.transform.scale(pygame.image.load("images/p2 down.png"), (30, 30)).convert_alpha()
    p1sbody = pygame.transform.scale(pygame.image.load("images/p2 body.png"), (30, 30)).convert_alpha()
    p1s = p1sleft
    # PLAYER 2 SPRITES
    direction2 = "RIGHT"
    p2sleft = pygame.transform.scale(pygame.image.load("images/p1 left.png"), (30, 30)).convert_alpha()
    p2sright = pygame.transform.scale(pygame.image.load("images/p1 right.png"), (30, 30)).convert_alpha()
    p2sup = pygame.transform.scale(pygame.image.load("images/p1 up.png"), (30, 30)).convert_alpha()
    p2sdown = pygame.transform.scale(pygame.image.load("images/p1 down.png"), (30, 30)).convert_alpha()
    p2sbody = pygame.transform.scale(pygame.image.load("images/p1 body.png"), (30, 30)).convert_alpha()
    score2img = pygame.transform.scale(pygame.image.load("images/score2.png"), (pcspecs[0]/8,pcspecs[1]/30)).convert_alpha()
    p2s = p2sleft
    global defvol
    if defvol :
        pygame.mixer.music.load("music/ingame music3.mp3")
        pygame.mixer.music.play()
    
    bground = pygame.transform.scale(pygame.image.load("images/image.jpg"), (pcspecs[0], pcspecs[1])).convert_alpha()
    snax, snay = 1200, 400
    snaxx, snayy = 100, 700
    velx = 0 
    vely = 0
    velxx = 0 
    velyy = 0
    foodx = random.randint(0, 1300)
    foody = random.randint(50, 700)
    score1 = 0 
    score2 = 0
    exit_game = False 
    game_over = False 
    winner = None
    snake1_list = []
    snake1_length = 1
    snake2_list = [100]
    snake2_length = 1
    wloc, hloc = [x for x in range(10, 1340, 10)], [x for x in range(55, 746, 10)]
    
    if(not os.path.exists("data/highscore.txt")) : 
      with open("data/highscore.txt", "w") as b : 
        b.write("0")
    with open("data/highscore.txt", "r") as f :
        high = f.read()
    
    while not exit_game :
        if game_over : 
            win.blit(gover, (360,120))
            win.blit(blimg, (0,53))
            win.blit(winner, (pcspecs[0]/3, pcspecs[1]/3))
            win.blit(resetimg, (pcspecs[0]/4, 1.5*pcspecs[1]/3))
            win.blit(menuimg, ((pcspecs[0]/4, 1.8*pcspecs[1]/3)))
            with open("data/highscore.txt", "w") as t: 
                t.write(str(high))     
            
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    exit_game = True
                
                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_RETURN : 
                        gameloop2()
                        
                    if event.key == pygame.K_ESCAPE : 
                        loadscreen()
        else : 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loadscreen()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d and direction2 != "LEFT":
                        velxx = 10
                        velyy = 0
                        direction2 = "RIGHT"
                    elif event.key == pygame.K_a and direction2 != "RIGHT":
                        velxx = -10
                        velyy = 0
                        direction2 = "LEFT"
                    elif event.key == pygame.K_w and direction2 != "DOWN":
                        velyy = -10
                        velxx = 0
                        direction2 = "UP"
                    elif event.key == pygame.K_s and direction2 != "UP":
                        velyy = 10
                        velxx = 0
                        direction2 = "DOWN"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and direction1 != "LEFT":
                        velx = 10
                        vely = 0
                        direction1 = "RIGHT"
                    elif event.key == pygame.K_LEFT and direction1 != "RIGHT":
                        velx = -10
                        vely = 0
                        direction1 = "LEFT"
                    elif event.key == pygame.K_UP and direction1 != "DOWN":
                        vely = -10
                        velx = 0
                        direction1 = "UP"
                    elif event.key == pygame.K_DOWN and direction1 != "UP":
                        vely = 10
                        velx = 0
                        direction1 = "DOWN"

            snax = snax + velx
            snay = snay + vely
            snaxx = snaxx + velxx
            snayy = snayy + velyy

            if direction1 == "RIGHT":
                p1s = p1sright
            elif direction1 == "LEFT":
                p1s = p1sleft
            elif direction1 == "UP":
                p1s = p1sup
            elif direction1 == "DOWN":
                p1s = p1sdown

            if direction2 == "RIGHT":
                p2s = p2sright
            elif direction2 == "LEFT":
                p2s = p2sleft
            elif direction2 == "UP":
                p2s = p2sup
            elif direction2 == "DOWN":
                p2s = p2sdown


            foodsound = pygame.mixer.Sound("music/foodsound.mp3")
            foodsound.set_volume(0.5)
            if abs(snax - foodx) < 30 and abs(snay - foody) < 30 : 
                foodsound.play(0)
                score1 += 1 
                foodx = random.choice(wloc)
                foody = random.choice(hloc)
                snake1_length += 2
            if abs(snaxx - foodx) < 30 and abs(snayy - foody) < 30 : 
                foodsound.play(0)
                score2 += 1 
                foodx = random.choice(wloc)
                foody = random.choice(hloc)
                snake2_length += 2


            win.blit(bground, (0,0))
            win.blit(foodimg, (foodx, foody))
            win.blit(borderimg, (0, 0))        
            win.blit(score1img, (20, pcspecs[1]/45))
            win.blit(colonimg, (200, pcspecs[1]/40))
            tex(str(score1), (0, 0, 0), pcspecs[0]/6, pcspecs[1]/75)
            win.blit(hscore, (pcspecs[0]/3+80, pcspecs[1]/45))
            win.blit(colonimg, (750, pcspecs[1]/40))
            tex(str(high), (0, 0, 0), 770, pcspecs[1]/75)
            win.blit(score2img, (pcspecs[0]-260, pcspecs[1]/45))
            win.blit(colonimg, (pcspecs[0]-80, pcspecs[1]/40))
            tex(str(score2), (0, 0, 0), pcspecs[0]-60, pcspecs[1]/75)
            if int(high) < score1 : 
                high = score1
            elif int(high) < score2 : 
                high = score2

            head1 = []
            head1.append(snax)
            head1.append(snay)    
            snake1_list.append(head1)
            
            head2 = []
            head2.append(snaxx)
            head2.append(snayy)    
            snake2_list.append(head2)

            if len(snake1_list) > snake1_length : 
                del snake1_list[0]
            if len(snake2_list) > snake2_length : 
                del snake2_list[0]

            if snax < 0 : 
                snax = 1350
            elif snax > 1350 : 
                snax = 0
            if snay > 750 : 
                snay = 52 
            elif snay <= 53 : 
                snay = 750
            
            if snaxx < 0 : 
                snaxx = 1350
            elif snaxx > 1350 : 
                snaxx = 0
            if snayy > 750 : 
                snayy = 52 
            elif snayy <= 53 : 
                snayy = 750

            
            if head2 in snake1_list[:-1] :
                game_over = True
                winner = pygame.transform.scale(pygame.image.load("images/winner1.png"), (pcspecs[0]/3,pcspecs[1]/20)).convert_alpha()
            if head1 in snake2_list[:-1] : 
                game_over = True
                winner = pygame.transform.scale(pygame.image.load("images/winner2.png"), (pcspecs[0]/3,pcspecs[1]/20)).convert_alpha()


            # WORKING OF SNAKES
            plot(win, snake1_list, p1sbody)
            plot(win, snake2_list, p2sbody)
            win.blit(p1s, tuple(snake1_list[-1]))
            win.blit(p2s, tuple(snake2_list[-1]))


        pygame.display.update()
        clock.tick(30)
    
    
    
    
loadscreen()
    
    
    