# # 14.练习 — 使用变量 (1/2)
# ## purple_pentagon.py
# 答案

import turtle
turtle.bgcolor('black') # 改变画布背景颜色为黑色，不要修改这句话
mary = turtle.Turtle()
lovely_color = "purple"
mary.color(lovely_color)
for side in [1, 2, 3, 4, 5]:
    mary.forward(100)
    mary.right(72)
