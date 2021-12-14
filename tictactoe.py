def tict():
    import pygame, sys
    import numpy as np
    pygame.mixer.pre_init()
    pygame.init()
    width = 600
    height = 600
    line_width =15
    board_rows = 3
    board_cols = 3
    square_size = width//board_cols
    circle_r = square_size//3
    circle_w = 15
    cross_w = 25
    space = square_size//4
    #color = RGB
    bg_color = (0, 0, 0)
    line_color = (20, 20, 20)
    circle_color = (250, 237, 39)
    cross_color = (255, 16, 240)
    green = (0, 250, 0)
    #screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TIC TAC TOE Multiplayer (Press R to play again!)")
    screen.fill(bg_color)
    #board
    board = np.zeros((board_rows, board_cols))

    def drawlines():
        #1 horizontal line
        pygame.draw.line(screen, line_color, (0, square_size), (width, square_size), line_width)
        #2 horizontal line
        pygame.draw.line(screen, line_color, (0, 2*square_size), (width, 2*square_size), line_width)
        #1 vertical line
        pygame.draw.line(screen, line_color, (square_size, 0), (square_size, height), line_width)
        #2 vertical line
        pygame.draw.line(screen, line_color, (2*square_size, 0), (2*square_size, height), line_width)

    def draw_figures():
        for row in range(board_rows):
            for col in range(board_cols):
                if board[row][col] == 1:
                    pygame.draw.circle(screen, circle_color, (int(col * square_size + square_size//2), int(row * square_size + square_size//2)), circle_r, circle_w)
                elif board[row][col] == 2:
                    pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + square_size - space), (col * square_size + square_size - space, row * square_size + space), cross_w)
                    pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + space), (col * square_size + square_size - space, row * square_size + square_size - space), cross_w)

    #mark squares for player
    def mark_square(row, col, player):
        board[row][col] = player

    #check available square(s)
    def avaiable_square(row, col):
        if board[row][col] == 0:
            return True
        else:
            return False

    #if board is full return True
    def isboard_full():
        for row in range(board_rows):
            for col in range(board_cols):
                if board[row][col] == 0:
                    return False
        return True

    def check_win(player):
        #vertical win check
        for col in range(board_cols):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                draw_vert_winline(col, player)
                return True
        #horizontal win check
        for row in range(board_rows):
            if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                draw_hori_winline(row, player)
                return True
        #ascending diag win check
        if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            draw_ascdiag_line(player)
            return True
        #descending diag win check
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            draw_desdiag_line(player)
            return True

        return False

    def draw_vert_winline(col, player):
        posX = col * square_size + square_size//2
        if player == 1:
            color = green
        elif player == 2:
            color = green

        pygame.draw.line(screen, color, (posX, 15), (posX, height - 15), 15)

    def draw_hori_winline(row, player):
        posY = row * square_size + square_size//2
        if player == 1:
            color = green
        elif player == 2:
            color = green

        pygame.draw.line(screen, color, (15, posY), (width - 15, posY), 15)

    def draw_ascdiag_line(player):
        if player == 1:
            color = green
        elif player == 2:
            color = green

        pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15), 15)

    def draw_desdiag_line(player):
        if player == 1:
            color = green
        elif player == 2:
            color = green

        pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), 15)

    def restart():
        screen.fill(bg_color)
        drawlines()
        player = 1
        for row in range(board_rows):
            for col in range(board_cols):
                board[row][col] = 0

    drawlines()

    player = 1
    gameover = False

    #mainloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.unpause()
                main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN and not gameover:

                mouseX = event.pos[0] #x
                mouseY = event.pos[1] #y
                
                click_row = int(mouseY // square_size)
                click_col = int(mouseX // square_size)

                if avaiable_square(click_row, click_col):
                    mark_square(click_row, click_col, player)
                    if check_win(player):
                        gameover = True
                    player = player % 2 + 1

                    draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    gameover = False
        pygame.display.update()
tict()