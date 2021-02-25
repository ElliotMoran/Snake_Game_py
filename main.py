#! pypy3
if __name__ == '__main__':
    import os
    import sys
    sys.path.insert(0, 'src/')
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    from game import Game

    game = Game()
    game.inizialization()
    game.main_loop()
