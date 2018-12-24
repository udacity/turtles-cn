# # 15.练习 — 使用变量 (2/2)
# ## purple_pentagon.py
# 答案

import turtle
mary = Turtle.Turtle()
color = "purple"
sides = [1, 2, 3, 4, 5]
angle = 72
distance = 100
mary.color(color)
for side in sides:
    mary.forward(distance)
    mary.right(angle)
