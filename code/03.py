# # 3.使用 turtle 绘画
# ## one.py

# 运行下方的代码

import turtle
turtle.bgcolor('black') # 改变画布背景颜色为黑色
george = turtle.Turtle()
george.color("yellow")
for side in [1, 2, 3, 4]:
    george.forward(100)
    george.right(90)
