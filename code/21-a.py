
# # 21.神秘的形状
# ## mystery.py
# 答案


import turtle
turtle.bgcolor('black') # 改变画布背景颜色为黑色，不要修改这句话

builder = turtle.Turtle()
builder.color("red")
builder.width(5)

angles = [-90, 0, 0, -90,
          135, 0, 0, 0, 
          90, 0, 0, 0,
          135, -90, 0, 0,
          90, 0, 0, 0]

for angle in angles:
    builder.right(angle)
    builder.forward(25)

