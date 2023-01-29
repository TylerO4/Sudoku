import pygame, sys
from constants import *
from sudoku_generator import *
from board import Board
import copy


def draw_game_start(screen):
    # Initialize title font
    start_title_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font(None, 50)
    # Color background
    screen.fill(BG_COLOR)
    # Initialize and draw title
    title_surface = start_title_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)
    # Initialize buttons
    # Initialize text first

    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))
    # Initialize button background color and text
    easy_surface = pygame.Surface((140, 50)) #easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20 is proportional to text size
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (32.5, 10))

    medium_surface = pygame.Surface((140, 50)) # size of rectangle
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (5, 10)) # position of words on rectangle

    hard_surface = pygame.Surface((140, 50))  # size of rectangle
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (30, 10))  # position of words on rectangle

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 4, HEIGHT // 2 + 50))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 1.33, HEIGHT // 2 + 50))
    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    # Checks if mouse is on start button
                    return  30 # If the mouse is on the start button, we can return to main
                elif medium_rectangle.collidepoint(event.pos):
                    return 40
                elif hard_rectangle.collidepoint(event.pos):
                    return 50

        pygame.display.update()

"""def draw_game_over(screen):
    game_over_font = pygame.font.Font(None, 40)
    screen.fill(BG_COLOR)
    if winner != 0:
        text = f'Player {winner} wins!'
    else:
        text = "No one wins!"
    game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)
    restart_surf = game_over_font.render(
'Press r to play again...', 0, LINE_COLOR)
    restart_rect = restart_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(restart_surf, restart_rect)
    #  Added key to return to main menu
    menu_surf = game_over_font.render(
        'Press m to return to the main menu...', 0, LINE_COLOR)
    menu_rect = menu_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(menu_surf, menu_rect)"""

def draw_lose_screen(screen):
    game_over_font = pygame.font.Font(None, 100)
    screen.fill(BG_COLOR)

    game_over_surf = game_over_font.render("Game Over :(", 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(center=(300, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)

    restart_text = button_font.render("Restart", 0, (255, 255, 255))

    # Initialize button background color and text
    restart_surface = pygame.Surface(
        (140, 50))  # easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20 is proportional to text size
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    # Initialize button rectangle
    restart_rectangle = restart_surface.get_rect(center=(300, HEIGHT // 2 + 50))
    # Draw buttons
    screen.blit(restart_surface, restart_rectangle)

def draw_win_screen(screen):
    win_font = pygame.font.Font(None, 100)
    screen.fill(BG_COLOR)

    win_surf = win_font.render("Game Won!", 0, LINE_COLOR)
    win_rect = win_surf.get_rect(center=(300, HEIGHT // 2 - 100))
    screen.blit(win_surf, win_rect)

    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    # Initialize button background color and text
    exit_surface = pygame.Surface(
        (140, 50))  # easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20 is proportional to text size
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (35, 10))

    # Initialize button rectangle
    exit_rectangle = exit_surface.get_rect(center=(300, HEIGHT // 2 + 50))
    # Draw buttons
    screen.blit(exit_surface, exit_rectangle)


def draw_ingame(screen):
    pygame.draw.rect(screen, (55, 118, 171), pygame.Rect(0, 600, 600, 100))
    # pygame.display.flip()
    button_font = pygame.font.Font(None, 50)
    quit_text = button_font.render("Quit", 0, (255, 255, 255))
    quit_surface = pygame.Surface((140, 50))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (32.5, 10))
    quit_rectangle = quit_surface.get_rect(center=(150, 650))

    reset_text = button_font.render("Reset", 0, (255, 255, 255))
    reset_surface = pygame.Surface((140, 50))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (22.5, 10))
    reset_rectangle = reset_surface.get_rect(center=(300, 650))

    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    restart_surface = pygame.Surface((140, 50))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = reset_surface.get_rect(center=(450, 650))

    screen.blit(quit_surface, quit_rectangle)
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)


if __name__ == '__main__':
    game_over = False

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    pygame.draw.rect(screen, (55, 118, 171), pygame.Rect(0, 600, 600, 100))

    button_font = pygame.font.Font(None, 50)

    quit_text = button_font.render("Quit", 0, (255, 255, 255))
    quit_surface = pygame.Surface((140, 50))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (32.5, 10))
    quit_rectangle = quit_surface.get_rect(center=(150, 650))

    reset_text = button_font.render("Reset", 0, (255, 255, 255))
    reset_surface = pygame.Surface((140, 50))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (22.5, 10))
    reset_rectangle = reset_surface.get_rect(center=(300, 650))

    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    restart_surface = pygame.Surface((140, 50))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = reset_surface.get_rect(center=(450, 650))

    screen.blit(quit_surface, quit_rectangle)
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)

    difficulty = draw_game_start(screen)  # Calls function to draw start screen
    print(difficulty)

    screen.fill(BG_COLOR)
    # draw_lines()
    # middle_cell = Cell('o', 1, 1, 200, 200)
    # middle_cell.draw(screen)
    board = Board(9, 9, WIDTH, BOARD_HEIGHT, screen, difficulty)
    board_reset = board.reset

    # board.print_board()
    board.draw()

    while True:
        # Drawing Rectangle
        for event in pygame.event.get():
            #board.screen.fill(BG_COLOR)
            #board.draw()

            draw_ingame(screen)

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if quit_rectangle.collidepoint(event.pos):
                    # If the mouse is on the quit button, exit the program
                    sys.exit()
                elif reset_rectangle.collidepoint(event.pos):
                    board.reset_board()
                    screen.fill(BG_COLOR)
                    board.draw()
                elif restart_rectangle.collidepoint(event.pos):
                    difficulty = draw_game_start(screen)
                    board.restart_board()
                    screen.fill(BG_COLOR)
                    board.draw()
                else:
                    clicked_row = int(event.pos[1] / SQUARE_SIZE)
                    clicked_col = int(event.pos[0] / SQUARE_SIZE)
                    print(clicked_row, clicked_col)
                    board.select(clicked_row, clicked_col)

            if event.type == pygame.KEYUP:
                num = None

                if event.key == pygame.K_LEFT:
                    clicked_col -= 1
                    print(clicked_col)
                    board.select(clicked_row, clicked_col)
                if event.key == pygame.K_RIGHT:
                    clicked_col += 1
                    print(clicked_col)
                    board.select(clicked_row, clicked_col)
                if event.key == pygame.K_UP:
                    clicked_row -= 1
                    print(clicked_row)
                    board.select(clicked_row, clicked_col)
                if event.key == pygame.K_DOWN:
                    clicked_row += 1
                    print(clicked_row)
                    board.select(clicked_row, clicked_col)

                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    num = 0
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    num = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    num = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    num = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    num = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    num = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    num = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    num = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    num = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    num = 9
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    num = None

                if num != None:
                    board.sketch(clicked_row, clicked_col, num)

                if event.key == pygame.K_RETURN:
                    temp = board.cells[clicked_row][clicked_col].sketched
                    board.mark_square(clicked_row, clicked_col, temp)

            if event.type == pygame.KEYDOWN:
                # if user presses r, return to main menu
                if event.key == pygame.K_r:
                    board.reset_all()
                    print(board.board)
                    print(board.reset)
                    screen.fill(BG_COLOR)
                    board.draw()
                if event.key == pygame.K_m:
                    # if the user presses m, return to the main menu
                    game_over = False
                    chip = 'x'
                    board.reset_all()
                    difficulty = draw_game_start(screen)
                    screen.fill(BG_COLOR)
                    board.draw()

            if board.board_is_full():
                if board.check_win():
                    draw_win_screen(screen)
                else:
                    draw_lose_screen(screen)

        # game is over
        if game_over:
            pygame.display.update()
            pygame.time.delay(1000)
        pygame.display.update()

