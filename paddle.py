class Paddle:
    """
    The canvas object is needed so the paddle object can create and
    move the paddle on the canvas. The canvas height lets the paddle know where
    it should be placed, which is at the bottom of the canvas. The width lets
    the paddle know how far to the left or right it can travel.
    """

    def __init__(self, canvas, canvas_height, canvas_width):
        self.__canvas = canvas
        self.__canvas_width = canvas_width

        # Create a rectangle representing the paddle. We can't give it any
        # coordinates yet since how wide it is depends on the difficulty
        # the user chooses.
        self.__canvas.create_rectangle(0, 0, 0, 0, tags='paddle')

        # These values depend on the difficulty the user chooses so
        # we can't assign a value to them yet.
        self.__moving_distance = 0
        self.__paddle_width = 0

        self.__middle_of_start_point = canvas_width // 2

        # Only need to use the left x coord to keep track of position.
        # Can't give these a value yet since how wide the paddle
        # is depends on the difficulty the user selects
        self.__left_x_coord = 0
        self.__max_left_x_coord = 0

        # Paddle height is 10
        self.__top_y_coord = canvas_height - 10
        self.__bottom_y_coord = canvas_height

        # Set controls
        self.__canvas.bind('<Left>', self.move_left)
        self.__canvas.bind('<Right>', self.move_right)
        self.__canvas.focus_set()

    @property
    def left_x_coord(self):
        return self.__left_x_coord

    @property
    def right_x_coord(self):
        return self.__left_x_coord + self.__paddle_width

    @property
    def top_y_coord(self):
        return self.__top_y_coord

    def set_color(self, color):
        # Use the canvas object to change the paddle's color
        self.__canvas.itemconfig('paddle', fill=color)

    def set_difficulty(self, difficulty):
        if difficulty == 'Easy':
            self.__left_x_coord = self.__middle_of_start_point - 50
            self.__paddle_width = 100
            self.__moving_distance = 10

        elif difficulty == 'Medium':
            self.__left_x_coord = self.__middle_of_start_point - 35
            self.__paddle_width = 70
            self.__moving_distance = 20

        else:  # Difficulty is hard
            self.__left_x_coord = self.__middle_of_start_point - 20
            self.__paddle_width = 40
            self.__moving_distance = 30

        self.__max_left_x_coord = self.__canvas_width - self.__paddle_width

    def place_on_canvas(self):
        self.__canvas.coords('paddle', self.__left_x_coord, self.__top_y_coord,
                             self.__left_x_coord + self.__paddle_width, self.__bottom_y_coord)

    def move_left(self, event):
        if self.__left_x_coord >= self.__moving_distance:
            self.__canvas.move('paddle', -self.__moving_distance, 0)
            self.__left_x_coord -= self.__moving_distance

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

    def move_right(self, event):
        if self.__left_x_coord <= (self.__max_left_x_coord - self.__moving_distance):
            self.__canvas.move('paddle', self.__moving_distance, 0)
            self.__left_x_coord += self.__moving_distance

        elif self.__left_x_coord < self.__max_left_x_coord:
            temp_moving_distance = self.__max_left_x_coord - self.__left_x_coord
            self.__canvas.move('paddle', temp_moving_distance, 0)
            self.__left_x_coord += temp_moving_distance
