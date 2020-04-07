import tkinter
from ball import Ball
from paddle import Paddle


class Game(tkinter.Frame):
    def __init__(self, root, height, width):
        super().__init__(root, height=height, width=width)
        self.__CANVAS_HEIGHT = 510

        top_frame = tkinter.Frame(self)
        self.__canvas = tkinter.Canvas(self, width=width, height=self.__CANVAS_HEIGHT)
        bottom_frame = tkinter.Frame(self)

        top_frame.place(relheight=0.05, relwidth=1)
        self.__canvas.place(rely=0.05, relheight=0.85)
        bottom_frame.place(rely=0.9, relheight=0.1, relwidth=1)

        self.__paddle = Paddle(self.__canvas, self.__CANVAS_HEIGHT, width)
        self.__ball = Ball(self.__canvas, self.__CANVAS_HEIGHT, width, self.__paddle.top_y_coord)

        self.__STARTING_NUMBER_OF_LIVES = 3
        self.__lives_left = self.__STARTING_NUMBER_OF_LIVES
        self.__score = 0

        self.__lives_label = tkinter.Label(top_frame, text=f'Lives left: {self.__lives_left}')
        self.__score_label = tkinter.Label(top_frame, text='Score: 0')

        self.__lives_label.place(relx=0.33, rely=0.5, anchor='center')
        self.__score_label.place(relx=0.67, rely=0.5, anchor='center')

        objective_label = tkinter.Label(bottom_frame, text='Move the paddle to prevent the ball '
                                                           'from hitting the bottom')
        controls_label = tkinter.Label(bottom_frame, text='Controls\nLeft Arrow - Move Left'
                                                          '        Right Arrow - Move Right'
                                                          '        Q - Quit')

        objective_label.place(relx=0.5, rely=0.2, anchor='center')
        controls_label.place(relx=0.5, rely=0.7, anchor='center')

        self.__quit = False
        # Make it so that when the user hits the q button during a game, the game quits.
        self.__canvas.bind('q', self.set_quit_true)

    def show(self):
        self.pack()

    def hide(self):
        self.pack_forget()

    def set_quit_true(self, event):
        self.__quit = True

    def set_colors(self, background_color, ball_color, paddle_color):
        self.__canvas.config(bg=background_color)
        self.__ball.set_color(ball_color)
        self.__paddle.set_color(paddle_color)

    def set_difficulties(self, difficulty):
        self.__ball.set_difficulty(difficulty)
        self.__paddle.set_difficulty(difficulty)
        self.__paddle.place_on_canvas()

    def play(self):
        while True:
            self.__ball.move()

            if self.__quit:
                self.__quit = False
                break

            if self.__ball.has_reached_left_or_right_wall:
                self.__ball.change_horizontal_direction()

            if self.__ball.has_reached_top_wall:
                self.__ball.change_vertical_direction()

            if self.__ball.has_reached_bottom_wall:
                if self.__lives_left == 1:
                    break
                self.decrement_lives()
                self.__ball.change_vertical_direction()

            if self.__ball.has_reached_paddle:
                if self.__ball.has_hit_paddle(self.__paddle.left_x_coord, self.__paddle.right_x_coord):
                    self.increment_score()
                    self.__ball.change_vertical_direction()

            self.update_canvas()

    # Canvas needs to be updated in each frame
    def update_canvas(self):
        self.__canvas.after(10)  # Set a pause for 10 milliseconds
        self.__canvas.update()

    def decrement_lives(self):
        self.__lives_left -= 1
        self.__lives_label.config(text=f'Lives left: {self.__lives_left}')

    def increment_score(self):
        self.__score += 1
        self.__score_label.config(text=f'Score: {self.__score}')

    def reset(self):
        self.__lives_left = self.__STARTING_NUMBER_OF_LIVES
        self.__lives_label.config(text=f'Lives left: {self.__lives_left}')

        self.__score = 0
        self.__score_label.config(text='Score: 0')

        self.__ball.reset()
