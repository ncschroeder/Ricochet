class Ball:
    """
    canvas_info is a dictionary containing a canvas object and the height and width
    of that canvas. The canvas object is needed so that the ball object can create and
    move the ball on the canvas. The height and width are needed so the ball object
    knows how far it can travel in all directions.

    The paddle top y coord is needed so the ball object knows when to check if it
    has hit the paddle.
    """
    def __init__(self, canvas_info, paddle_top_y_coord):

        self.__canvas = canvas_info['canvas']
        canvas_width = canvas_info['width']
        canvas_height = canvas_info['height']

        self.__diameter = 20

        # Starting coordinates
        self.__left_x_coord = 0
        self.__right_x_coord = self.__diameter
        self.__top_y_coord = 0
        self.__bottom_y_coord = self.__diameter

        # The left x and top y coordinates are the only ones that get changed
        # so we need to set their limits
        self.__max_left_x_coord = canvas_width - self.__diameter
        self.__max_top_y_coord = canvas_height - self.__diameter

        # Use the canvas object given to us to create an oval in the top left corner
        self.__canvas.create_oval(self.__left_x_coord, self.__top_y_coord, self.__right_x_coord,
                                  self.__right_x_coord, tags='ball')

        # Can't set a value for speeds yet since they change based
        # on what difficulty the user selects
        self.__vertical_speed = 0
        self.__horizontal_speed = 0

        # Paddle meet point is for the top y coordinate of the ball
        paddle_meet_point = paddle_top_y_coord - self.__diameter

        """
        Need a paddle meet range because the speed below will be a floating point number 
        so that means that when the ball moves, as seen in a method below, the top_y_coord
        variable of the ball will change by a floating point number in each frame. When 
        the ball meets the paddle, the top_y_coord variable of the ball will be close to 
        the paddle meet point but not exact.
        """
        self.__paddle_meet_range_min = paddle_meet_point - 0.1
        self.__paddle_meet_range_max = paddle_meet_point + 0.1

        self.__easy_speed = round(paddle_meet_point / 200, 3)
        self.__medium_speed = round(paddle_meet_point / 150, 3)
        self.__hard_speed = round(paddle_meet_point / 100, 3)

    def set_color(self, color):
        # Use the canvas object to change the ball's color
        self.__canvas.itemconfig('ball', fill=color)

    def set_difficulty(self, difficulty):

        if difficulty == 'Easy':
            self.__vertical_speed = self.__easy_speed
            self.__horizontal_speed = self.__easy_speed

        elif difficulty == 'Medium':
            self.__vertical_speed = self.__medium_speed
            self.__horizontal_speed = self.__medium_speed

        else:  # Difficulty is hard
            self.__vertical_speed = self.__hard_speed
            self.__horizontal_speed = self.__hard_speed

    def move(self):
        # The left x and top y coordinates variables change to keep track of where
        # the ball is so we know when to have the ball change direction in the
        # methods below.
        self.__left_x_coord += self.__horizontal_speed
        self.__top_y_coord += self.__vertical_speed

        # Use the canvas object to move the ball. Note that a positive horizontal
        # speed means the ball is moving right and a positive vertical speed means
        # the ball is moving down.
        self.__canvas.move('ball', self.__horizontal_speed, self.__vertical_speed)

    @property
    def has_reached_left_or_right_wall(self):
        return self.__left_x_coord >= self.__max_left_x_coord or self.__left_x_coord <= 0

    @property
    def has_reached_top_wall(self):
        return self.__top_y_coord <= 0

    @property
    def has_reached_bottom_wall(self):
        return self.__top_y_coord >= self.__max_top_y_coord

    @property
    def has_reached_paddle(self):
        return self.__vertical_speed > 0 and self.__paddle_meet_range_min \
               <= self.__top_y_coord <= self.__paddle_meet_range_max

    def has_hit_paddle(self, paddle_left_x_coord, paddle_right_x_coord):
        return paddle_left_x_coord <= self.__left_x_coord <= paddle_right_x_coord or \
               paddle_left_x_coord <= self.__left_x_coord + self.__diameter <= paddle_right_x_coord

    def change_vertical_direction(self):
        self.__vertical_speed *= -1

    def change_horizontal_direction(self):
        self.__horizontal_speed *= -1

    def reset(self):
        # Only need to reset these 2 variables since they are the ones that change
        self.__left_x_coord = 0
        self.__top_y_coord = 0
        # Use the canvas object to put the ball back in the top left corner
        self.__canvas.coords('ball', self.__left_x_coord, self.__top_y_coord,
                             self.__right_x_coord, self.__bottom_y_coord)
