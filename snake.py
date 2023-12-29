from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:




    def __init__(self):

        self.squares = []
        self.create_snake()
        self.head = self.squares[0]


    def create_snake(self):


        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.squares.append(new_segment)

    def extend(self):
        #add a new segment

        self.add_segment(self.squares[-1].position())


    def move(self):


        for seg_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[seg_num - 1].xcor()
            new_y = self.squares[seg_num - 1].ycor()
            self.squares[seg_num].goto(new_x, new_y)

        self.squares[0].forward(MOVE_DISTANCE)


    def snake_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


    def snake_left(self):
        if self.head.heading() != 0:
            self.squares[0].setheading(180)


    def snake_up(self):
        if self.head.heading() != 270:
            self.squares[0].setheading(90)


    def snake_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


    def reset(self):
        for seg in self.squares:
            seg.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

