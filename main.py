#! pypy3
if __name__ == '__main__':
    from game import Game
    game = Game()
    game.initialization()
    game.main_loop()
