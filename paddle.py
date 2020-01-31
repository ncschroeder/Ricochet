class Paddle:
    """
    canvas_info is a dictionary containing a canvas object and the height and width
    of that canvas. The canvas object is needed so the paddle object can create and
    move the paddle on the canvas. The height lets the paddle know where it should be
    placed, which is at the bottom of the canvas. The width lets the paddle know
    how far to the left or right it can travel.
    """
    def __init__(self, canvas_info):

        self.__canvas = canvas_info['canvas']
        canvas_width = canvas_info['width']
        canvas_height = canvas_info['height']

        # Use the canvas object given to us to create a rectangle representing
        # the paddle. We can't give it any coordinates yet since how wide it is
        # depends on the difficulty the user chooses.
        self.__canvas.create_rectangle(0, 0, 0, 0, tags='paddle')

        # Moving distance depends on the difficulty the user chooses so we can't
        # assign a value to it yet.
        self.__moving_distance = 0

        # These half paddle widths get added to the middle of the start point in
        # the set_difficulty method to form the coordinates
        self.__middle_of_start_point = canvas_width // 2
        self.__easy_half_paddle_width = 50
        self.__medium_half_paddle_width = 35
        self.__hard_half_paddle_width = 20

        # Can't give x coordinates a value yet since how wide the paddle is depends
        # on the difficulty the user selects
        self.__left_x_coord = 0
        self.__right_x_coord = 0

        self.__max_right_x_coord = canvas_width

        paddle_height = 10
        self.__top_y_coord = canvas_height - paddle_height
        self.__bottom_y_coord = canvas_height

        # Set controls
        self.__canvas.bind('<Left>', self.move_left)
        self.__canvas.bind('<Right>', self.move_right)
        self.__canvas.focus_set()

    def set_color(self, color):
        # Use the canvas object to change the paddle's color
        self.__canvas.itemconfig('paddle', fill=color)

    def set_difficulty(self, difficulty):
        if difficulty == 'Easy':
            self.__left_x_coord = self.__middle_of_start_point - self.__easy_half_paddle_width
            self.__right_x_coord = self.__middle_of_start_point + self.__easy_half_paddle_width
            self.__moving_distance = 10

        elif difficulty == 'Medium':
            self.__left_x_coord = self.__middle_of_start_point - self.__medium_half_paddle_width
            self.__right_x_coord = self.__middle_of_start_point + self.__medium_half_paddle_width
            self.__moving_distance = 20

        else:  # Difficulty is hard
            self.__left_x_coord = self.__middle_of_start_point - self.__hard_half_paddle_width
            self.__right_x_coord = self.__middle_of_start_point + self.__hard_half_paddle_width
            self.__moving_distance = 30

    def place_on_canvas(self):
        # Use the canvas object to place the paddle in the right spot on the canvas
        self.__canvas.coords('paddle', self.__left_x_coord, self.__top_y_coord,
                             self.__right_x_coord, self.__bottom_y_coord)

    def get_top_y_coord(self):
        return self.__top_y_coord

    def get_left_x_coord(self):
        return self.__left_x_coord

    def get_right_x_coord(self):
        return self.__right_x_coord

    def move_left(self, event):
        if self.__left_x_coord >= self.__moving_distance:
            self.__canvas.move('paddle', -self.__moving_distance, 0)
            self.__left_x_coord -= self.__moving_distance
            self.__right_x_coord -= self.__moving_distance

        elif self.__left_x_coord > 0:
            """
            The following code runs when the paddle is close to the left wall 
            but not touching it and if the paddle was to move the normal 
            moving distance then it would go off screen so this code prevents 
            that. The code in the elif statement in the move_right method does
            the same thing but for the right wall.
            """
            temp_moving_distance = self.__left_x_coord
            self.__canvas.move('paddle', -temp_moving_distance, 0)
            self.__left_x_coord -= temp_moving_distance
            self.__right_x_coord -= temp_moving_distance

    def move_right(self, event):
        if self.__right_x_coord < (self.__max_right_x_coord - self.__moving_distance):
            self.__canvas.move('paddle', self.__moving_distance, 0)
            self.__left_x_coord += self.__moving_distance
            self.__right_x_coord += self.__moving_distance

        elif self.__right_x_coord < self.__max_right_x_coord:
            temp_moving_distance = self.__max_right_x_coord - self.__right_x_coord
            self.__canvas.move('paddle', temp_moving_distance, 0)
            self.__left_x_coord += temp_moving_distance
            self.__right_x_coord += temp_moving_distance
