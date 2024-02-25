import pygame

# File Paths (CHANGE THIS)
FILE_PATH = '/Users/gsundaram/Desktop/Hackathon Stuff'

#game size
NUM_COLS = 10
NUM_ROWS = 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = NUM_COLS * CELL_SIZE, NUM_ROWS  * CELL_SIZE

#side bar size
SIDEBAR_WIDTH = 200
PREV_HEIGHT_FRAC = 0.7
SCORE_HEIGHT_FRAC = 1 - PREV_HEIGHT_FRAC

#window
PADDING = 20
GAP = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + GAP * 3
WINDOW_HEIGHT = GAME_HEIGHT + GAP * 2

# game behaviour
UPDATE_START_SPEED = 150
MOVE_WAIT_TIME = 120
ROTATE_WAIT_TIME = 200
OFFSET = pygame. Vector2 (NUM_COLS // 2, -1)

# colors
YELLOW = '#f1e60d'
RED = '#e51b20'
BLUE = '#204b9b'
GREEN = '#65b32e'
PURPLE = '#7b217f'
CYAN = '#6cc6d9'
ORANGE = '#f07e13'
GRAY = '#1C1C1C'
LINE_COLOR = '#000000'
BACKGROUND_COLOR = '#FFFFFF'

TETROMINOS = {
    'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': PURPLE},
    'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': YELLOW},
    'J': {'shape': [(0,0), (0,-1), (0,1), (-1,1)], 'color': BLUE},
    'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'color': ORANGE},
    'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'color': CYAN},
    'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': GREEN},
    'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': RED}
}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}