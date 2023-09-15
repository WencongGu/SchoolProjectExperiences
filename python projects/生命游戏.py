import random
import time
import os


class GameOfLife():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[random.randint(0,1) for x in range(width)] for y in range(height)]

    def evolve(self):
        new_board = [[0 for x in range(self.width)] for y in range(self.height)]

        for i in range(self.width):
            for j in range(self.height):
                neighbor_sum = 0
                for ii in range(-1,2):
                    for jj in range(-1,2):
                        if ii == 0 and jj == 0:
                            continue
                        if i+ii < 0 or i+ii >= self.width or j+jj < 0 or j+jj >= self.height:
                            neighbor_sum += 0
                        else:
                            neighbor_sum += self.board[i+ii][j+jj]

                if self.board[i][j] == 1:
                    if neighbor_sum < 2 or neighbor_sum > 3:
                        new_board[i][j] = 0
                    else:
                        new_board[i][j] = 1
                else:
                    if neighbor_sum == 3:
                        new_board[i][j] = 1

        self.board = new_board

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] == 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print('')
        print('')


if __name__ == '__main__':
    game = GameOfLife(50, 50)
    while True:
        game.display()
        game.evolve()
        time.sleep(0.1)
