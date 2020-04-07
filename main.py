import tkinter
from menu import Menu
from game import Game


def play():
    menu.hide()
    game.set_colors(menu.background_color, menu.ball_color, menu.paddle_color)
    game.set_difficulties(menu.difficulty)
    game.show()
    game.play()
    game.hide()
    game.reset()
    menu.generate_random_colors()
    menu.show()


root = tkinter.Tk()
root.title('Ricochet')

HEIGHT = 600
WIDTH = 800

menu = Menu(root, HEIGHT, WIDTH, play)
game = Game(root, HEIGHT, WIDTH)

root.mainloop()
