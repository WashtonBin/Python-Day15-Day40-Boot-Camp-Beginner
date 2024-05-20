import colorgram
import random
import turtle as t
"""extract color from an image"""
# rgb_colors = []
# colors = colorgram.extract('hirst-white-paper.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(210, 153, 64), (240, 232, 237), (39, 86, 172), (103, 160, 209), (229, 199, 57), (180, 61, 100), (148, 19, 59), (199, 115, 157), (143, 181, 10), (189, 72, 39), (51, 110, 95), (65, 53, 42), (12, 66, 135), (57, 52, 67), (187, 78, 103), (60, 50, 64), (96, 107, 170), (221, 172, 191), (140, 167, 162), (171, 187, 220), (183, 101, 85), (228, 174, 167), (72, 64, 52), (184, 194, 198), (104, 140, 131), (173, 205, 199), (70, 61, 57)]
t.colormode(255)
t.speed(0)
t.ht()
t.setheading(225)
t.penup()
t.forward(300)
t.setheading(0)
num_of_dots = 100


for i in range(1, num_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)




t.exitonclick()

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_tuple = (r, g, b)
#     return random_tuple
#
#
#
# for _ in range(10):
#     print(random_color())