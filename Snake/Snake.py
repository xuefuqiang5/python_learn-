import pygame
import random
from collections import deque
# macro define 


RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WINDOW_SIZE = (600, 600)
LEFT = 1
RIGHT = 2
UP = 3 
DOWN = 4
UNIT_SIZE = 20
WIDTH_UNIT = WINDOW_SIZE[0] // UNIT_SIZE
HEIGH_UNIT = WINDOW_SIZE[1] // UNIT_SIZE

painter_list = []


direction_dir = {
    LEFT: (0, 1),
    RIGHT: (0, -1),
    UP: (1, 0),
    DOWN: (-1, 0)
}


class Screen:
    def __init__(self):
        pass
        
        
    def screen_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]), pygame.NOFRAME)

    def run(self):
        self.screen_init()
        # running = True
        # while running:
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #running = False
        self.screen.fill(WHITE)
        pygame.display.flip()
        for item in painter_list:
            pygame.draw.rect(self.screen, BLACK, (item[0] * 20, item[1] * 20, 20, 20))
        painter_list.clear()

class Food:
    def __init__(self):
        self.food_position = (random.randint(0, WIDTH_UNIT), random.randint(0, HEIGH_UNIT))
        painter_list.append(self.food_position)
        


class Snake:
    def __init__(self) -> None:
        self.length = 5 
        self.position = (WIDTH_UNIT // 2, HEIGH_UNIT // 2)
        self.direction = random.randint(1, 4)
        self.body = deque((self.position[0], self.position[1] + i) for i in range(1, self.length))
        
    def snake_growth(self):
        self.body.append(self.body[0] + direction_dir[self.direction])
    def Snake_move(self, dirtion = LEFT):
        self.position += direction_dir[dirtion]
        self.body.append(self.position)
        self.body.popleft()
    

    def Snake_dead(self):
        for item in self.body:
            if self.direction == item:
                return False
        bool_list = [self.position == (i, HEIGH_UNIT) for i in WIDTH_UNIT]
        if bool_list.index(1) != None:
            return False
        bool_list = [self.position == (WIDTH_UNIT, i) for i in HEIGH_UNIT]
        if bool_list.index(1) != None:
            return False
        bool_list = [self.position == (0, i) for i in HEIGH_UNIT]
        if bool_list.index(1) != None:
            return False
        bool_list = [self.position == (i, 0) for i in WIDTH_UNIT]
        if bool_list.index(1) != None:
            return False
        return True
class Game:
    def __init__(self) -> None:
        self.Screen1 = Screen()
        self.Snake1 = Snake()
        self.Food1 = Food()
        pass
    def game_open(self):
        run = True
        while True:
            painter_list.append(self.Food1.food_position)
            for item in self.Snake1.body:
                painter_list.append(item)
            self.Screen1.run()
            


        self.Snake.Snake_move()
    def game_over():
        pass


if __name__ == "__main__":
    game = Game()
    game.game_open()