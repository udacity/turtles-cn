# # 6.更改颜色
# ## two.py

import turtle
turtle.bgcolor('black') # 改变画布背景颜色为黑色，不要修改这句话
amy = turtle.Turtle()
amy.color("yellow")
for side in [1, 2, 3, 4]:
    amy.forward(100)
    amy.right(90)
