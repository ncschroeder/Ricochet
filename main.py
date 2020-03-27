import tkinter
from ball import Ball
from paddle import Paddle
from menu import Menu
from game_screen import GameScreen


def play():
    game_screen.set_background_color(menu.background_color)

    ball.set_color(menu.ball_color)
    ball.set_difficulty(menu.difficulty)

    paddle.set_color(menu.paddle_color)
    paddle.set_difficulty(menu.difficulty)
    paddle.place_on_canvas()

    menu.hide()
    game_screen.show()

    while True:
        ball.move()

        if game_screen.user_wants_to_quit:
            game_screen.reset_quit_bool()
            break

        if ball.has_reached_left_or_right_wall:
            ball.change_horizontal_direction()

        if ball.has_reached_bottom_wall:
            if game_screen.one_life_left:
                break
            game_screen.decrement_lives()
            ball.change_vertical_direction()

        if ball.has_reached_top_wall:
            ball.change_vertical_direction()

        if ball.has_reached_paddle:
            if ball.has_hit_paddle(paddle.left_x_coord, paddle.right_x_coord):
                game_screen.increment_score()
                ball.change_vertical_direction()

        game_screen.update_canvas()

    game_screen.reset()
    ball.reset()

    game_screen.hide()
    menu.generate_random_colors()
    menu.show()



root = tkinter.Tk()
root.title('Ricochet')

HEIGHT = 600
WIDTH = 800
CANVAS_HEIGHT = 510
# canvas width is same as WIDTH

menu = Menu(root, HEIGHT, WIDTH, play)
game_screen = GameScreen(root, HEIGHT, WIDTH, CANVAS_HEIGHT)
paddle = Paddle(game_screen.canvas, CANVAS_HEIGHT, WIDTH)
ball = Ball(game_screen.canvas, CANVAS_HEIGHT, WIDTH, paddle.top_y_coord)

root.mainloop()
