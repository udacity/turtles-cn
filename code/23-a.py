# # 23.练习 — Turtle 方法
# ## turtle_methods.py
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

# Draw a red line
# 画一条红线（red）
amy.color("red")
amy.forward(50)

# Move forward without drawing anything
# 向前移动且不画任何东西
amy.penup()
amy.forward(50)
amy.pendown()

# Draw an orange line
# 画一条橙色线（orange）
amy.color("orange")
amy.forward(50)

# Move forward without drawing anything
# 向前移动且不画任何东西
amy.penup()
amy.forward(50)
amy.pendown()

# Draw a yellow line
# 画一条黄线（yellow）
amy.color("yellow")
amy.forward(50)
