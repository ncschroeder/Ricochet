import tkinter


class GameScreen:
    def __init__(self, root, height, width):
        self.__main_frame = tkinter.Frame(root, height=height, width=width)

        self.__canvas_height = height * 0.85
        self.__canvas_width = width

        top_frame = tkinter.Frame(self.__main_frame)
        self.__canvas = tkinter.Canvas(self.__main_frame, width=self.__canvas_width,
                                       height=self.__canvas_height)
        bottom_frame = tkinter.Frame(self.__main_frame)

        top_frame.place(relheight=0.05, relwidth=1)
        self.__canvas.place(rely=0.05, relheight=0.85)
        bottom_frame.place(rely=0.9, relheight=0.1, relwidth=1)

        self.__starting_number_of_lives = 3
        self.__lives_left = self.__starting_number_of_lives
        self.__score = 0

        self.__lives_label = tkinter.Label(top_frame, text='Lives left: ' +
                                                           str(self.__lives_left))
        self.__score_label = tkinter.Label(top_frame, text='Score: 0')

        self.__lives_label.place(relx=0.33, rely=0.5, anchor='center')
        self.__score_label.place(relx=0.67, rely=0.5, anchor='center')

        objective_label = tkinter.Label(bottom_frame, text='Move the paddle to prevent the ball'
                                                           ' from hitting the bottom')
        controls_label = tkinter.Label(bottom_frame, text='Controls\nLeft Arrow - Move Left'
                                                          '        Right Arrow - Move Right'
                                                          '        Q - Quit')

        objective_label.place(relx=0.5, rely=0.2, anchor='center')
        controls_label.place(relx=0.5, rely=0.7, anchor='center')

        self.__quit_bool = False
        """
        Make it so that when the user hits the q button, the game quits.
        Throughout each frame of the game, quit_bool is checked and the
        game quits if quit_bool is ever true.
        """
        self.__canvas.bind('q', self.set_quit_bool_true)

    def set_quit_bool_true(self, event):
        self.__quit_bool = True

    def set_quit_bool_false(self):
        self.__quit_bool = False

    @property
    def user_wants_to_quit(self):
        return self.__quit_bool

    def show(self):
        self.__main_frame.pack()

    def hide(self):
        self.__main_frame.pack_forget()

    def set_canvas_color(self, color):
        self.__canvas.config(bg=color)

    # Canvas info is for the ball and paddle objects
    @property
    def canvas_info(self):
        return {'canvas': self.__canvas, 'width': self.__canvas_width,
                'height': self.__canvas_height}

    # Canvas needs to be updated in each frame
    def update_canvas(self):
        self.__canvas.after(10)  # Set a pause for 10 milliseconds
        self.__canvas.update()

    @property
    def one_life_left(self):
        return self.__lives_left == 1

    def decrement_lives(self):
        self.__lives_left -= 1
        self.__lives_label.config(text='Lives left: ' + str(self.__lives_left))

    def increment_score(self):
        self.__score += 1
        self.__score_label.config(text='Score: ' + str(self.__score))

    def reset(self):
        self.__lives_left = self.__starting_number_of_lives
        self.__lives_label.config(text='Lives left: ' + str(self.__lives_left))

        self.__score = 0
        self.__score_label.config(text='Score: 0')
