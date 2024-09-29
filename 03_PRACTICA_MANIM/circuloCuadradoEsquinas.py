from manim import *

class SquareAndCircleInTheCorners(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(WHITE, opacity=0.5)  # set the color and transparency

        circle2 = Circle()  # create a circle
        circle2.set_fill(YELLOW, opacity=0.5)  # set the color and transparency


        square = Square()  # create a square
        square.set_fill(GREEN, opacity=0.5)  # set the color and transparency'
        square.shift(LEFT * 6 + UP * 3)

        square2 = Square()  # create a square
        square2.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        circle.next_to(square, DOWN, buff=4)  # set the position
        square2.next_to(circle, RIGHT, buff=10)  # set the position
        circle2.next_to(square, RIGHT, buff=10)  # set the position
        #circle.next_to(square2, DOWN, buff=0.5)  # set the position


        self.play(Create(square), Create(circle),Create(square2), Create(circle2))  # show the shapes on screen