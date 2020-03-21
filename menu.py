import tkinter
from random import randrange


class Menu(tkinter.Frame):
    # The play function is passed in so that it will be called when the play button
    # on the menu is clicked
    def __init__(self, root, height, width, play_function):
        super().__init__(root, height=height, width=width)
        #self.__main_frame = tkinter.Frame(root, height=height, width=width)

        # Colors are for the ball, paddle, and background color option menus in the menu
        self.__colors = ('Bisque', 'Black', 'Blue', 'Cyan', 'Dark Goldenrod', 'Deep Pink',
                         'Gainsboro', 'Gold', 'Green', 'Light Pink', 'Midnight Blue',
                         'Olive Drab', 'Orange', 'Pale Green', 'Purple', 'Red', 'Saddle Brown',
                         'Salmon', 'Sea Green', 'Sky Blue', 'Slate Gray', 'Thistle',
                         'Turquoise', 'Violet Red', 'White', 'Yellow')

        title = tkinter.Label(self, text='Ricochet', font=(None, 30))
        title.place(relx=0.5, rely=0.2, relheight=0.1, anchor='center')

        self.__difficulty = tkinter.StringVar()
        self.__difficulty.set('Easy')

        difficulty_label = tkinter.Label(self, text='Difficulty\n(This will affect '
                                                                 'ball speed and paddle size)')
        easy_button = tkinter.Radiobutton(self, text='Easy', value='Easy',
                                          variable=self.__difficulty)
        medium_button = tkinter.Radiobutton(self, text='Medium', value='Medium',
                                            variable=self.__difficulty)
        hard_button = tkinter.Radiobutton(self, text='Hard', value='Hard',
                                          variable=self.__difficulty)

        difficulty_label.place(relx=0.25, rely=0.55, anchor='center')
        easy_button.place(relx=0.15, rely=0.6, anchor='center')
        medium_button.place(relx=0.25, rely=0.6, anchor='center')
        hard_button.place(relx=0.35, rely=0.6, anchor='center')

        self.__ball_color = tkinter.StringVar()
        ball_color_label = tkinter.Label(self, text='Ball Color')
        ball_color_menu = tkinter.OptionMenu(self, self.__ball_color, *self.__colors)

        self.__paddle_color = tkinter.StringVar()
        paddle_color_label = tkinter.Label(self, text='Paddle Color')
        paddle_color_menu = tkinter.OptionMenu(self, self.__paddle_color, *self.__colors)

        self.__background_color = tkinter.StringVar()
        background_color_label = tkinter.Label(self, text='Background Color')
        background_color_menu = tkinter.OptionMenu(self, self.__background_color, *self.__colors)

        ball_color_label.place(relx=0.7, rely=0.45, anchor='center')
        ball_color_menu.place(relx=0.7, rely=0.5, anchor='center')
        paddle_color_label.place(relx=0.85, rely=0.45, anchor='center')
        paddle_color_menu.place(relx=0.85, rely=0.5, anchor='center')
        background_color_label.place(relx=0.775, rely=0.58, anchor='center')
        background_color_menu.place(relx=0.775, rely=0.63, anchor='center')

        generate_random_colors_button = tkinter.Button(self, text='Generate Random Colors',
                                                       command=self.generate_random_colors)
        self.__play_button = tkinter.Button(self, text='Play', command=play_function)

        generate_random_colors_button.place(relx=0.775, rely=0.75, anchor='center')
        self.__play_button.place(relx=0.5, rely=0.85, anchor='center')

        self.generate_random_colors()
        self.show()

    def show(self):
        self.pack()

    def hide(self):
        self.pack_forget()

    def get_difficulty(self):
        return self.__difficulty.get()

    def get_ball_color(self):
        return self.__ball_color.get()

    def get_paddle_color(self):
        return self.__paddle_color.get()

    def get_background_color(self):
        return self.__background_color.get()

    def generate_random_colors(self):
        background_color_index = randrange(len(self.__colors))
        self.__background_color.set(self.__colors[background_color_index])

        # The following code prevents the ball and paddle from
        # becoming the same color as the background
        ball_color_index = randrange(len(self.__colors))
        while ball_color_index == background_color_index:
            ball_color_index = randrange(len(self.__colors))
        self.__ball_color.set(self.__colors[ball_color_index])

        paddle_color_index = randrange(len(self.__colors))
        while paddle_color_index == background_color_index:
            paddle_color_index = randrange(len(self.__colors))
        self.__paddle_color.set(self.__colors[paddle_color_index])
