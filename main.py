#! pypy3
if __name__ == '__main__':
    import sys
    sys.path.insert(0, 'src/')
    from game import Game
    
    game = Game()
    game.inizialization()
    game.main_loop()
