# # 26.练习 — 嵌套循环
# ## nested_loops.py

# In[ ]:


# 请在这里写下你的答案
import turtle
turtle.bgcolor('black') # 改变画布背景颜色为黑色，不要修改这句话
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.forward(-140)
amy.pendown()

# Draw three shapes of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
    amy.color(prettycolor)
    amy.forward(50)
    amy.penup()
    amy.forward(50)
    amy.pendown()
