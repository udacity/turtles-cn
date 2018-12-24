# # 19.列表和循环
# ## squiral.py


import turtle
turtle.bgcolor('black') # 改变画布背景颜色为黑色，不要修改这句话

lengths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

dizzy = turtle.Turtle()
dizzy.color("blue")
dizzy.width(5)

for length in lengths:
    dizzy.forward(length)
    dizzy.right(90)
