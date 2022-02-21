import pygame as pg

GRID_NUM = 19 # max numbers of chesses
GRID_LENGTH = 30 # pixel size of a grid for a chess
CHESS_RADIUS = 12 # pixel size of radius

pg.init()
screen = pg.display.set_mode((GRID_NUM * GRID_LENGTH, GRID_NUM * GRID_LENGTH))

'''draw a background'''
game_surface = pg.Surface(screen.get_size())
game_surface.fill((170, 238, 187))

'''draw lines to form grids'''
for grid_x_idx in range(GRID_NUM):
    pg.draw.line(
        game_surface, 
        color = (125,125,125), 
        start_pos = (grid_x_idx * GRID_LENGTH, 0),
        end_pos = (grid_x_idx * GRID_LENGTH, game_surface.get_size()[1])
    )
for grid_x_idx in range(GRID_NUM):
    pg.draw.line(
        game_surface, 
        color = (125,125,125), 
        start_pos = (0, grid_x_idx * GRID_LENGTH),
        end_pos = (game_surface.get_size()[0], grid_x_idx * GRID_LENGTH)
    )

'''draw background to the screen'''
screen.blit(game_surface,(0,0))

'''create chess Surface'''
chess_grids = []

def draw_chess(mouse_pos, chess_color):     
    '''draw a chess based on player's mouse position'''
    sqaure_x_idx = mouse_pos[0] // GRID_LENGTH
    sqaure_y_idx = mouse_pos[1] // GRID_LENGTH
    if [sqaure_x_idx, sqaure_y_idx] in chess_grids:
        return chess_color
    chess_grids.append([sqaure_x_idx, sqaure_y_idx])
    chess_center_x =  GRID_LENGTH * sqaure_x_idx + GRID_LENGTH / 2
    chess_center_y =  GRID_LENGTH * sqaure_y_idx + GRID_LENGTH / 2
    pg.draw.circle(game_surface, chess_color, (chess_center_x,chess_center_y), CHESS_RADIUS)
    return [255-x for x in chess_color]
    
def main():
    chess_color = [0,0,0]
    while 1:
        draw = False
        # main loop
        for event in pg.event.get():
            # event handling
            if event.type == pg.QUIT:
                # player quit game
                return

            if event.type == pg.MOUSEBUTTONDOWN:
                # player lay a chess
                chess_color = draw_chess(pg.mouse.get_pos(), chess_color)
                draw = True

        '''update screen'''
        screen.blit(game_surface,(0,0)) # display game
        if not draw:
            # lay a chess on mouse postion if player didn't lay a chess
            pg.draw.circle(screen, chess_color, pg.mouse.get_pos(), CHESS_RADIUS)
        pg.display.flip()

    # pg.quit()
    

if __name__ == '__main__':
    main()

