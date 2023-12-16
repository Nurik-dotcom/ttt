import pygame as pg, sys
from pygame.locals import *
import time, random, copy, csv

XO = None  
move=None
    
TTT= [0,0,0,0,0,0,0,0,0]
    
game_save=[]
    
 


stage=[] 
move_stage=[] 
moves=[]  

winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
line_color = (10, 10, 10)


pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")


opening = pg.image.load('tic_tac_opening.png')
x_img = pg.image.load('x.png')
o_img = pg.image.load('o.png')


x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))
opening = pg.transform.scale(opening, (width, height + 100))
def game_opening():
    screen.fill(white)
    screen.blit(opening, (0, 0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

    
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
    
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)

    draw_status()

def draw_status(): 
    global XO, draw, game_save, filename

    if winner is None and XO == -1:
        message = "X's Turn"
    if winner == -1:
        message = "X won!"
        # into_file()

    if winner is None and XO == 1:
        message = "0's Turn"
    if winner == 1:
        message = "0 won!"
        # into_file()

    if draw:
        message = 'Game Draw!'
        # into_file()

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()
    time.sleep(0.4)

def check_win():
    global TTT, winner, draw

    
    for row in range(0, 7, 3):  
        if ((TTT[row] == TTT[row + 1] == TTT[row + 2]) and (TTT[row] != 0)):
            
            winner = TTT[row]
            pg.draw.line(screen, (250, 0, 0), (0, (row/3 + 1) * height / 3 - height / 6), \
                         (width, (row/3 + 1) * height / 3 - height / 6), 4)
            break

    
    for col in range(0, 3, 1):  
        if (TTT[col] == TTT[col + 3] == TTT[col + 6]) and (TTT[col] != 0):
            
            winner = TTT[col]
            
            pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0), \
                         ((col + 1) * width / 3 - width / 6, height), 4)
            break

    
    if (TTT[0] == TTT[4] == TTT[8]) and (TTT[0] != 0):
        
        winner = TTT[0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)

    if (TTT[2] == TTT[4] == TTT[6]) and (TTT[2] != 0):
        
        winner = TTT[2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

    if TTT.count(0) == 0 and winner is None:  
        draw = True

    draw_status()
    
def DrawXO(): 
    global TTT, XO, move
    TTT[move] = XO
    # for_file()
   
    if move == 0:
        posx = 30
        posy = 30
    if move == 1:
        posx = width / 3 + 30
        posy = 30
    if move == 2:
        posx = width / 3 * 2 + 30
        posy = 30

    if move == 3:
        posx = 30
        posy = height / 3 + 30
    if move == 4:
        posx = width / 3 + 30
        posy = height / 3 + 30
    if move == 5:
        posx = width / 3 * 2 + 30
        posy = height / 3 + 30

    if move == 6:
        posx = 30
        posy = height / 3 * 2 + 30
    if move == 7:
        posx = width / 3 + 30
        posy = height / 3 * 2 + 30
    if move == 8:
        posx = width / 3 * 2 + 30
        posy = height / 3 * 2 + 30

    if XO == -1:
        screen.blit(x_img, (posx, posy))
        print(posx, posy)
    else:
        screen.blit(o_img, (posx, posy))
    XO = -1*XO
    # pg.display.update()
    check_win()

def user_click(): 
    global move
    move=None
    
    x, y = pg.mouse.get_pos()
    print(x, y, height, width)
    if (y < height / 3) and (x < width / 3):
        move = 0
    elif (y < height / 3) and (x < width / 3 * 2):
        move = 1
    elif (y < height / 3) and (x < width):
        move = 2

    elif (y < height / 3 * 2) and (x < width / 3):
        move = 3
    elif (y < height / 3 * 2) and (x < width / 3 * 2):
        move = 4
    elif (y < height / 3 * 2) and (x < width):
        move = 5

    elif (y < height) and (x < width / 3):
        move = 6
    elif (y < height) and (x < width / 3 * 2):
        move = 7
    elif (y < height) and (x < width):
        move = 8
    
def reset_game():
    global TTT, winner, XO, draw
    time.sleep(0.5)
    XO = -1
    draw = False
    winner = None
    TTT= [0,0,0,0,0,0,0,0,0]
    game_opening()
    draw_status()


# def for_file(): 
#     global TTT, game_save, move
#     if TTT2.count(0)<=8:
#         TTT2.append((move + 1) * XO)                             
                                      
#         TTT3 = copy.deepcopy(TTT2)  
#         game_save.append(TTT3)  
#         TTT2.pop()  

# def game_save_length(): 
    
#     global game_save, XO
#     for item in game_save:
#         if draw is True: 
#             item.append(9)  
#         else:
#             item.append(len(game_save)) 
    
# def into_file(): 
#     global game_save
#     game_save_length() 
    

#     file.close()
#     game_save.clear()  
    
def from_file(): 
    global TTT, move, XO
    # filename = "data.csv"  
    # with open(filename, "r") as file:
    #     reader = csv.reader(file)
                

        # if len(stage)==0: 


    for q in range(0, len(stage), 1):
        if stage[q] == min(stage): 
            moves.append(move_stage[q]) 
    
    if len(moves)==0: 
        move = None 
    elif len(moves)==1:
        move = moves[0]-1
    else: 
        while True:
            move = moves[random.randint(0, len(moves)-1)]-1
            if TTT[move] == 0:
                break
    stage.clear()
    move_stage.clear()
    moves.clear()


def X_player(): 
    global TTT, XO, move, winner, draw

    while (True):  
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if XO == -1: 
                if event.type == MOUSEBUTTONDOWN:
                    user_click()  
                    if move == None:
                        continue
                    else:
                        if (TTT[move] == 0):
                            # TTT2 = copy.deepcopy(TTT)  
                            DrawXO()
            if XO == 1 and draw is False and winner is None: 
                # TTT2 = copy.deepcopy(TTT)  
                
                from_file()  
                if move is None:
                    while True:
                        if TTT[4] == 0:  
                            move = 4
                            break
                        else:  
                            move = random.randint(0, 8)
                            if TTT[move] == 0:
                                break
                DrawXO()
        if (winner or draw):
            reset_game()
        pg.display.update()
        # CLOCK.tick(fps)
def O_player(): 
    global TTT, XO, move, winner, draw

    while (True):  
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if XO == -1:
                # TTT2 = copy.deepcopy(TTT)  
                
                # from_file()  
                if move is None:
                    while True:
                        move = random.randint(0, 8)
                        if TTT[move] == 0:
                            break
                
                DrawXO()
            if XO == 1 and draw is False and winner is None:
                if event.type == MOUSEBUTTONDOWN:
                    user_click()  
                    if move == None:
                        continue
                    else:
                        if (TTT[move] == 0):
                            # TTT2 = copy.deepcopy(TTT)  
                            DrawXO()
        if (winner or draw):
            reset_game()
        pg.display.update()
        CLOCK.tick(fps)

def menu_XO():
    screen.fill(white)
    
    pg.draw.line(screen, RED, (width / 3, height/3), (width / 3, height/3*2), 4)
    pg.draw.line(screen, RED, (width / 3 * 2, height/3), (width / 3 * 2, height/3*2), 4)
    pg.draw.line(screen, RED, (1, height / 3), (1, height / 3 * 2), 4)
    pg.draw.line(screen, RED, (width-3, height / 3), (width-3, height / 3 * 2), 4)
    
    pg.draw.line(screen, RED, (0, height / 3), (width/3+2, height / 3), 4)
    pg.draw.line(screen, RED, (0, height / 3 * 2), (width/3+2, height / 3 * 2), 4)
    pg.draw.line(screen, RED, (width / 3*2, height / 3), (width, height / 3), 4)
    pg.draw.line(screen, RED, (width / 3*2, height / 3 * 2), (width, height / 3 * 2), 4)
    screen.blit(x_img, (30, 160))
    screen.blit(o_img, (290, 160))
    font = pg.font.Font(None, 80)
    text = font.render("X or O ?", 1, (255, 255, 255))
    
    screen.fill((RED), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()

def menu_click():
    global XO
    XO = None
    
    x, y = pg.mouse.get_pos()
    

    if (y < height / 3 * 2) and (y > height / 3 * 1) and (x < width / 3) and (x > 0):
        XO = -1
    elif (y < height / 3 * 2) and (y > height / 3 * 1) and (x < width) and (x > width / 3 * 2):
        XO = 1

while XO is None:  
    for event in pg.event.get():
        menu_XO()
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            menu_click()  
            if XO == None:
                continue
            else:
                if XO != None:
                    if XO == -1:
                        message = "X - player"
                    if XO == 1:
                        message = "O - player"

                    font = pg.font.Font(None, 60)
                    text = font.render(message, 1, (255, 255, 255))

                    
                    screen.fill((BLACK), (0, 400, 500, 100))
                    text_rect = text.get_rect(center=(width / 2, 500 - 50))
                    screen.blit(text, text_rect)
                    pg.display.update()
                    time.sleep(1.5)
                    break

game_opening()
if XO==-1:
    X_player()
elif XO==1:
    XO=-1 
    O_player()