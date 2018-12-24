# # 15.练习 — 使用变量 (2/2)
# ## purple_pentagon.py
# 答案

import turtle
turtle.bgcolor('black') # 改变画布背景颜色为黑色，不要修改这句话
mary = turtle.Turtle()
color = "purple"
sides = [1, 2, 3, 4, 5]
angle = 72
distance = 100
mary.color(color)
for side in sides:
    mary.forward(distance)
    mary.right(angle)
