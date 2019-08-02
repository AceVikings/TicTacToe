import pygame

clock = pygame.time.Clock()
board = [[None,None,None],
         [None,None,None],
         [None,None,None]]
i = 0
j = 0
counter = 0
turn_count = 1

def row_win():
    global board
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] !=None:
            if  board[row][0] == 1:
                return True,True
            else:
                return True,False
    else:
        return False,False
def col_win():
    global board
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] !=None:
            if  board[col][0] == 1:
                return True,True
            else:
                return True,False
    else:
        return False,False
def diag_win():
    global board
    if ((board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][0])) and board[1][1] != None:
        if board[1][1] == 1:
            return True, True
        else:
            return True, False
    else:
        return False, False

def check_win():
    if row_win()[0] or col_win()[0] or diag_win()[0]:
        return True
def next_move():
    global board,turn_count
    change_count = 0
    for row in range(3):
        for column in range(3):
            if board[row][column] == None:
                board[row][column] = 0
                if check_win():
                    change_count += 1
                    break
                else:
                    board[row][column] = None

                if change_count > 0:
                    break
    if change_count == 0:
        for row in range(3):
            for column in range(3):
                if board[row][column] == None:
                    board[row][column] = 1
                    if check_win():
                        board[row][column] = 0
                        change_count += 1
                        break
                    else:
                        board[row][column] = None
            if change_count > 0:
                break
    for row in range(3):
        for column in range(3):
            if change_count == 0:
                if board[1][1] == None:
                    board[1][1] = 0
                    change_count += 1
                elif board[row][column] == None:
                    board[row][column] = 0
                    change_count += 1

    turn_count += 1
    #
    # else:
    #     for row in range(3):
    #         for column in range(3):
    #             if board[row][column] == None:
    #                 board[row][column] = 0
    #                 break




# def possibilities():
#     global board
#
#     win_comp = 0
#     win_player = 0
#     count = 1
#     for row in range(3):
#         for column in range(3):
#             if board[row][column] == None:
#                 for r in range(3):
#                     for c in range(3):
#                         board[r][c] = 1
#                         if check_win()[0] and not check_win()[1]:
#                             board[r][c] = 0






pygame.init()
font = pygame.font.Font('freesansbold.ttf',50)
win = pygame.display.set_mode((740, 700))
pygame.display.set_caption("Tic Tac Toe")
def redraw():
    global i,j
    global counter
    win.fill((0,0,0))
    for row in range(3):
        for column in range(3):
            text = font.render('_', True, (255,255,255))
            win.blit(text, (200+(row*60), 150+(column*60)))
    if counter%2 == 0:
        for row in range(3):
            for column in range(3):
                if board[row][column] == None and row == i and column == j:
                    text = font.render('x', True, (255,255,255))
                    win.blit(text, (200+(row*60), 150+(column*60)))
    for row in range(3):
        for column in range(3):
            if board[row][column] == 1:
                text = font.render('x', True, (255, 255, 255))
                win.blit(text, (200 + (row * 60), 150 + (column * 60)))
    for row in range(3):
        for column in range(3):
            if board[row][column] == 0:
                text = font.render('o', True, (255, 255, 255))
                win.blit(text, (200 + (row * 60), 150 + (column * 60)))
    if check_win():
        text = font.render('Someone Won', True, (255, 255, 255))
        win.blit(text, (150, 100))
    pygame.display.update()

run = True
while run:
    clock.tick(80)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_DOWN:
                    if j+1 < 3:
                        j += 1

                if event.key == pygame.K_UP:
                    if j - 1 >= 0:
                        j -= 1
                if event.key == pygame.K_RIGHT:
                    if i < 3 :
                        i += 1
                if event.key == pygame.K_LEFT:
                    if i > 0:
                        i -= 1
                if event.key == pygame.K_SPACE:
                    board[i][j] = 1
                    turn_count += 1
            except:
                pass
        if turn_count % 2 == 0 and turn_count <=9:
            next_move()


    counter += 1
    redraw()

pygame.quit()