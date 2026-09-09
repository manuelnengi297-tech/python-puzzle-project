import pygame
import board
import movement_logic
import shuffle
pygame.init()
tile_size = 100
size = board.choose_size()
dictionary = shuffle.shuffle(size)
number_of_columns = board.num_of_columns(dictionary)
number_of_rows = board.num_of_rows(dictionary)
width = tile_size * number_of_columns
height = tile_size * number_of_rows
screen = pygame.display.set_mode((width, height))
running = True
font = pygame.font.Font(None, 50)
def pixel_to_tile(x,y):
    row = y // tile_size
    column = x // tile_size
    co_ordinate = (row, column)
    return co_ordinate
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            r0, c0 = movement_logic.find_blank(dictionary)
            if event.key == pygame.K_UP:
                move = (r0 + 1, c0)
                movement_logic.apply_move(dictionary, move)
            elif event.key == pygame.K_DOWN:
                move = (r0 - 1, c0)
                movement_logic.apply_move(dictionary, move)
            elif event.key == pygame.K_LEFT:
                move = (r0, c0 + 1)
                movement_logic.apply_move(dictionary, move)
            elif event.key == pygame.K_RIGHT:
                move = (r0, c0 - 1)
                movement_logic.apply_move(dictionary, move)
            else:
                pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            move = pixel_to_tile(x, y)
            movement_logic.apply_move(dictionary, move)
    screen.fill((255, 255, 255))  
    for coordinate, piece in dictionary.items():
        if piece == "_":
            pass
        else:
            r, c = coordinate
            x = c * tile_size
            y = r * tile_size
            rectangle = (x, y, tile_size, tile_size) 
            color = (70, 130, 180)
            pygame.draw.rect(screen, color, rectangle)
            text = font.render(str(piece), True, (0, 0, 0))
            screen.blit(text, (x + (tile_size // 2), y + (tile_size // 2)))
    pygame.display.flip()
    
