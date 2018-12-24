# # 26.练习 — 嵌套循环
# ## nested_loops.py

# In[ ]:


# 请在这里写下你的答案
import turtle
amy = Turtle.Turtle()

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
