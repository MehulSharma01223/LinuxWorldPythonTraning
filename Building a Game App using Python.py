# Tic-tac-to-
#This Python project implements a graphical Tic-Tac-Toe game (also called X/O) using the Pygame library. It allows two players to play on the same computer by clicking on the grid to place their X or O.
import pygame, sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 700))  # extra space for scoreboard
pygame.display.set_caption("Tic-Tac-Toe (X/O)")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Board settings
size = 200
board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

player = "X"
font = pygame.font.Font(None, 100)
score_font = pygame.font.Font(None, 40)

# Scoreboard
score = {"X": 0, "O": 0}

# Winning combination coordinates
win_combo = []

def draw_board():
    screen.fill(WHITE)
    # Draw grid
    pygame.draw.line(screen, BLACK, (size, 0), (size, 600), 5)
    pygame.draw.line(screen, BLACK, (2*size, 0), (2*size, 600), 5)
    pygame.draw.line(screen, BLACK, (0, size), (600, size), 5)
    pygame.draw.line(screen, BLACK, (0, 2*size), (600, 2*size), 5)
    
    # Draw X and O
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                color = BLUE if board[row][col] == "X" else RED
                text = font.render(board[row][col], True, color)
                screen.blit(text, (col*size + 70, row*size + 50))
    
    # Draw scoreboard
    score_text = score_font.render(f"Score - X: {score['X']}  O: {score['O']}", True, BLACK)
    screen.blit(score_text, (10, 610))
    
    # Draw restart button
    pygame.draw.rect(screen, GRAY, (400, 610, 180, 60))
    restart_text = score_font.render("Restart", True, BLACK)
    screen.blit(restart_text, (420, 625))

def check_winner():
    global win_combo
    # Rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            win_combo = [(i,0), (i,1), (i,2)]
            return board[i][0]
    # Columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != "":
            win_combo = [(0,i), (1,i), (2,i)]
            return board[0][i]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        win_combo = [(0,0),(1,1),(2,2)]
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        win_combo = [(0,2),(1,1),(2,0)]
        return board[0][2]
    # Draw
    if all(board[row][col] != "" for row in range(3) for col in range(3)):
        return "Draw"
    return None

def highlight_winner():
    for row, col in win_combo:
        pygame.draw.rect(screen, (0,255,0), (col*size, row*size, size, size), 10)

def reset_board():
    global board, player, win_combo
    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]
    player = "X"
    win_combo = []

# Main loop
run = True
winner = None
while run:
    draw_board()
    if win_combo:
        highlight_winner()
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and winner is None:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_y < 600:  # board click
                row = mouse_y // size
                col = mouse_x // size
                if board[row][col] == "":
                    board[row][col] = player
                    winner = check_winner()
                    if winner == "X" or winner == "O":
                        score[winner] += 1
                    player = "O" if player == "X" else "X"
            elif 400 <= mouse_x <= 580 and 610 <= mouse_y <= 670:  # restart button
                reset_board()
                winner = None
    
    # Show winner message
    if winner:
        if winner != "Draw":
            msg = f"{winner} Wins!"
        else:
            msg = "It's a Draw!"
        win_text = score_font.render(msg, True, BLACK)
        screen.blit(win_text, (200, 650))
    
    clock.tick(30)
