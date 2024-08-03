import turtle as t
from turtle import Turtle


class RectangleTurtle():
    def __init__(self,
                 x_cord: int,
                 y_cord: int,
                 length: int,
                 breadth: int,
                 name: str):
        self.turtle = Turtle()
        self.length = length
        self.breadth = breadth
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.name = name

    def draw_self(self):
        self.turtle.pencolor('red')   # color of the border (const)
        self.turtle.pensize(10)   # pensize  (const)
        self.turtle.penup()
        self.turtle.goto(self.x_cord, self.y_cord)
        self.turtle.pendown()
        self.turtle.forward(self.length)  # length of rect
        self.turtle.rt(90)
        self.turtle.forward(self.breadth)  # breadth of rect
        self.turtle.rt(90)
        self.turtle.forward(self.length)
        self.turtle.goto(self.x_cord, self.y_cord)

    def give_dims(self):
        self.turtle.penup()
        x_text = self.x_cord + (self.length / 2)
        y_text = self.y_cord - (self.breadth / 2)
        self.turtle.goto(x_text, y_text)
        self.turtle.pendown()
        self.turtle.write(f"""The length of {self.name} rectangle 
                        is {self.length} & breadth is {self.breadth}""")

    def locate_home(self):
        self.turtle.penup()
        x_text = self.x_cord + 15
        y_text = self.y_cord + 15 
        self.turtle.pendown()
        self.turtle.goto(x_text, y_text)
        self.turtle.write(f"""The x_ord of {self.name} rectangle 
                          is {self.x_cord} & y_ord is {self.y_cord}""")

    def get_center(self):
        # get the coords and add half of length and breadth
        x_cen = self.x_cord + self.length / 2
        y_cen = self.y_cord - self.breadth / 2
        return x_cen, y_cen

    def connect_centers(self, other):
        # lift pen_up
        self.turtle.penup()
        # get self center
        my_center = self.get_center()
        # go to the center
        self.turtle.goto(my_center)
        # get other's center
        other_center = other.get_center()
        # put pen down
        self.turtle.pendown()
        # draw line to other center
        self.turtle.goto(other_center)


def build_rectangle(myTurtle: t.Turtle,
                    x_cord: int,
                    y_cord: int,
                    length: int,
                    breadth: int):
    myTurtle.pencolor('red')   # color of the border (const)
    myTurtle.pensize(10)   # pensize  (const)
    myTurtle.penup()
    myTurtle.goto(x_cord, y_cord)
    myTurtle.pendown()
    # the rectangle is getting built
    myTurtle.forward(length)  # length of rect
    myTurtle.rt(90)
    myTurtle.forward(breadth)  # breadth of rect
    myTurtle.rt(90)
    myTurtle.forward(length)
    myTurtle.goto(x_cord, y_cord)
    print('Done')


if __name__ == '__main__':
    t1 = t.Turtle('turtle')  # we have to initialize

    tem = input("Press enter when ready...")
    # t1.pencolor('red')   # color of the border (const)
    # t1.pensize(10)   # pensize  (const)
    # t1.forward(200)  # length of rect
    # t1.rt(90)
    # t1.forward(100)  # breadth of rect
    # t1.rt(90)
    # t1.forward(200)
    # t1.home()        # co-ordinates of the home 
    # print('Done')
    # build_rectangle(myTurtle=t1,
                    # x_cord=50,
                    # y_cord=150,
                    # length=125,
                    # breadth=250)
    # build_rectangle(myTurtle=t1,
                    # x_cord=200,
                    # y_cord=300,
                    # length=100,
                    # breadth=75)
    rec1 = RectangleTurtle(50, 150, 125, 250, 'rect1')
    rec2 = RectangleTurtle(200, 300, 100, 75, 'rect2')
    rec1.draw_self()
    rec2.draw_self()
    rec1.give_dims()
    rec2.locate_home()
    t.mainloop()
