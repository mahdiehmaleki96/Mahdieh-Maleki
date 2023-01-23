import turtle

t = turtle.Turtle()

def draw_square(length):
    for i in range(0,4):
        t.forward(length)
        t.right(90)

draw_square(100)
    
