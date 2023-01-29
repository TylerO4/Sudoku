import random
import copy
import pygame
from constants import *
from sudoku_generator import *
from cell import Cell
class Board:
    def __init__(self, rows, cols, width, height, screen, difficulty):
        self.rows = rows
        self.difficulty = difficulty
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.board = generate_sudoku(9, difficulty)
        self.reset = copy.deepcopy(self.board)

        self.cells = [[Cell(self.board[i][j], i, j, self.height//self.rows, self.width//self.cols) for j in range(cols)] for i in range(rows)]

    def initialize_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append("-")
            board.append(row)
        return board

    def print_board(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                print(self.board[i][j], end=" ")
            print()

    def reset_all(self):
        self.board = copy.deepcopy(self.reset)
        for i in range(9):
            for j in range(9):
                self.cells[i][j].sketched = None
        self.update_cells()

    def valid_in_row(self, row, num):
        if self.board[row].count(num) > 1:
            return False
        else:
            return True

    def valid_in_col(self, col, num):
        new_list = []
        for i in self.board:
            new_list.append(i[col])
        if new_list.count(num) > 1:
            return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        new_list = []
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                new_list.append(self.board[i][j])
        if new_list.count(num) > 1:
            return False
        return True

    def check_win(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.valid_in_row(i, self.board[i][j]) == False:
                    return False
                if self.valid_in_col(i, self.board[i][j]) == False:
                    return False

        for x in range(0, 9):
            if self.valid_in_box(0, 0, x) == False:
                return False
            if self.valid_in_box(0, 3, x) == False:
                return False
            if self.valid_in_box(0, 6, x) == False:
                return False
            if self.valid_in_box(3, 0, x) == False:
                return False
            if self.valid_in_box(3, 3, x) == False:
                return False
            if self.valid_in_box(3, 6, x) == False:
                return False
            if self.valid_in_box(6, 0, x) == False:
                return False
            if self.valid_in_box(6, 3, x) == False:
                return False
            if self.valid_in_box(6, 6, x) == False:
                return False

        return True

    def draw(self): # 66.6 is for the spacing of the lines
        # draw lines

        for i in range(0, 10):
            if i == 3 or i == 6:
                pygame.draw.line(self.screen, LINE_COLOR, (0, 66.6 * i),
                                 (WIDTH, 66.6 * i), LINE_WIDTH+3)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (0, 66.6 * i),
                             (WIDTH, 66.6 * i), LINE_WIDTH)
        # draw vertical lines
        for i in range(0, 10):
            if i == 3 or i == 6:
                pygame.draw.line(self.screen, LINE_COLOR, (66.6 * i, 0),
                             (66.6 * i, BOARD_HEIGHT), LINE_WIDTH+3)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (66.6 * i, 0),
                                 (66.6 * i, BOARD_HEIGHT), LINE_WIDTH)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.screen)
                self.cells[i][j].draw(self.screen)

    def mark_square(self, row, col, num):
        print('mark square', num)
        self.board[row][col] = num
        self.cells[row][col].sketched = None
        self.update_cells()
        #pygame.display.update()
        for i in range(self.rows):
            for j in range(self.cols):
                pass
                #self.cells[i][j].draw(self.screen)

    def sketch(self, row, col, value):
        print("sketch run", value)
        self.cells[row][col].set_sketched_value(value)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.screen)

    def select(self, row, col):
        self.screen.fill(BG_COLOR)
        self.draw()
        cell_rect = self.cells[row][col]
        pygame.draw.rect(self.screen, (55, 118, 171), pygame.Rect(0, 600, 600, 100))
        # pygame.display.flip()
        pygame.draw.rect(self.screen, (55, 118, 171), pygame.Rect(0, 600, 600, 100))
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

        self.screen.blit(quit_surface, quit_rectangle)
        self.screen.blit(reset_surface, reset_rectangle)
        self.screen.blit(restart_surface, restart_rectangle)
        pygame.draw.rect(self.screen, RED, (66.6 * col, 66.6 * row, cell_rect.width + 2, cell_rect.height +2), 5)
        #pygame.display.update()


    def update_cells(self):
        self.cells = [[Cell(self.board[i][j], i, j, self.height//self.rows,
                            600//self.cols, self.cells[i][j].sketched) for j in range(self.cols)] for i in range(self.rows)]


    def available_square(self, row, col):
        return self.board[row][col] == '-'

    """def check_if_winner(self, chip_type):
        for i in range(self.rows):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][2] == chip_type:
                return True
        for j in range(self.cols):
            if self.board[0][j] == self.board[1][j] and self.board[1][j] == self.board[2][j] and self.board[2][j] == chip_type:
                return True
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[2][2] == chip_type:
            return True
        if self.board[2][0] == self.board[1][1] == self.board[0][2] == chip_type:
            return True
        return False"""

    def board_is_full(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 0 :
                    return False
        return True

    def reset_board(self):
        self.board = self.reset
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].sketched = None
        self.update_cells()

    def restart_board(self):
        self.board = generate_sudoku(9, self.difficulty)
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].sketched = None
        self.update_cells()
