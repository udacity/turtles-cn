# # 25.练习 — 更多循环变量 (2/2)
# ## more_loops.py

# 答案

import turtle
turtle.bgcolor('black') # 改变画布背景颜色为黑色，不要修改这句话
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
# 使线条宽度加粗，以便更容易看到线条
amy.width(5)

# Move back without drawing anything
# 向后移动且不画任何东西
amy.penup()
amy.back(140)
amy.pendown()

# Draw three lines of different colors, with space in between
#绘制三条不同颜色的线，线与线之间用空格间隔
for prettycolor in ["red", "orange", "yellow"]:
    amy.color(prettycolor)
    amy.forward(50)
    amy.penup()
    amy.forward(50)
    amy.pendown()
