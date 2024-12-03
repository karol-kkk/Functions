import turtle
import figures

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

def draw_square_at(x, y, length):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    figures.draw_square(pen, length)

def draw_triangle_at(x, y, length):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    figures.draw_triangle(pen, length)

def draw_rectangle_at(x, y, length_a, length_b):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    figures.draw_rectangle(pen, length_a, length_b)


draw_square_at(-150, 150, 100)   
draw_square_at(50, 150, 100)    

draw_triangle_at(-150, 50, 100) 
draw_triangle_at(50, 50, 100)    

draw_rectangle_at(-150, -100, 150, 80) 
draw_rectangle_at(50, -100, 150, 80)    

pen.hideturtle()
window.mainloop()
