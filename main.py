def main():
    import tkinter
    from ball import Ball
    from paddle import Paddle
    from menu import Menu
    from game_screen import GameScreen

    # Create a graphical user interface
    root = tkinter.Tk()
    root.title('Ricochet')

    HEIGHT = 600
    WIDTH = 800

    global menu, game_screen, paddle, ball
    # Instantiate all objects
    menu = Menu(root, HEIGHT, WIDTH, play)
    game_screen = GameScreen(root, HEIGHT, WIDTH)
    paddle = Paddle(game_screen.canvas_info)
    ball = Ball(game_screen.canvas_info, paddle.get_top_y_coord())

    # Make it so the program runs until the user closes the graphical user interface
    root.mainloop()


def play():
    game_screen.set_canvas_color(menu.get_background_color())

    ball.set_color(menu.get_ball_color())
    ball.set_difficulty(menu.get_difficulty())

    paddle.set_color(menu.get_paddle_color())
    paddle.set_difficulty(menu.get_difficulty())
    paddle.place_on_canvas()

    menu.hide()
    game_screen.show()

    while True:
        ball.move()

        if game_screen.user_wants_to_quit:
            """
            This conditional statement is true when the user hits the q button which
            causes the quit_bool in the GameScreen class to be set true. We need 
            quit_bool back to false since if we don't, the conditional statement would 
            be true and if the user was to try to start another game, that game would
            immediately end due to this code having a break statement.
            """
            game_screen.set_quit_bool_false()
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
            if ball.has_hit_paddle(paddle.get_left_x_coord(), paddle.get_right_x_coord()):
                game_screen.increment_score()
                ball.change_vertical_direction()

        game_screen.update_canvas()

    game_screen.reset()
    ball.reset()

    game_screen.hide()
    menu.generate_random_colors()
    menu.show()


main()
