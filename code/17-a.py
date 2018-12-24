# # 17.练习 — 基本循环
# ## triangle.py
# 答案

import turtle
turtle.bgcolor('black') # 改变画布背景颜色为黑色，不要修改这句话
juno = turtle.Turtle()
juno.color("white")

for side in [1, 2, 3]:
    juno.forward(100)
    juno.left(120)
