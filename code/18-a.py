# # 18.练习 — 将列表赋值给变量
# ## lists_and_variables.py
# 答案

import turtle
turtle.bgcolor('black') # 改变画布背景颜色为黑色，不要修改这句话
amy = turtle.Turtle()
amy.color("cyan")

some_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for item in some_list:
    amy.forward(50)
    amy.right(30)
